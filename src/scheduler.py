import asyncio
from typing import Optional

from arbitrage import compare_prices
from fetchers import ccxt_exchanges, uniswap


class PriceScanner:
    def __init__(self, interval: float = 60.0):
        """
        Initialize the price scanner with a specified interval in seconds.

        Args:
            interval: Time between price checks in seconds (default: 60.0)
        """
        self.interval = interval
        self._task: Optional[asyncio.Task] = None
        self._running = False

    async def _scan_prices(self) -> None:
        """Execute one full price scan cycle."""
        # Get prices from all CCXT exchanges
        exchange_prices = await ccxt_exchanges.get_all_prices()

        # Get Uniswap price
        uniswap_price = await uniswap.get_eth_price()

        # Print all prices
        print("\nExchange Prices:")
        for exchange, price in exchange_prices.items():
            print(f"{exchange.title()} ETH/USDT price: {price}")
        print(f"Uniswap ETH/USDT price: {uniswap_price}")

        # Compare prices between exchanges
        print("\nArbitrage Opportunities:")
        exchanges = list(exchange_prices.keys())
        for i in range(len(exchanges)):
            for j in range(i + 1, len(exchanges)):
                exchange_a = exchanges[i]
                exchange_b = exchanges[j]
                price_a = exchange_prices[exchange_a]
                price_b = exchange_prices[exchange_b]

                arbitrage = compare_prices(exchange_a, price_a, exchange_b, price_b)
                if arbitrage:
                    print(f"\n{exchange_a.title()} vs {exchange_b.title()}:")
                    print(f"Action: {arbitrage['action']}")
                    print(f"Spread: {arbitrage['spread']}%")
                    print(f"{exchange_a.title()} price: {arbitrage['price_a']}")
                    print(f"{exchange_b.title()} price: {arbitrage['price_b']}")

    async def _run_periodic(self) -> None:
        """Run the price scanner periodically."""
        while self._running:
            try:
                await self._scan_prices()
            except Exception as e:
                print(f"Error during price scan: {str(e)}")
            await asyncio.sleep(self.interval)

    def start(self) -> None:
        """Start the periodic price scanner."""
        if not self._running:
            self._running = True
            self._task = asyncio.create_task(self._run_periodic())

    def stop(self) -> None:
        """Stop the periodic price scanner."""
        if self._running:
            self._running = False
            if self._task:
                self._task.cancel()
                self._task = None
