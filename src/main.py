import asyncio

from arbitrage import compare_prices
from fetchers import ccxt_exchanges, uniswap


async def main():
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


if __name__ == "__main__":
    asyncio.run(main())
