from typing import Dict, List

import ccxt.async_support as ccxt

# List of exchanges to monitor
SUPPORTED_EXCHANGES = ["binance", "kucoin", "huobi", "okx", "bybit", "gateio", "kraken", "coinbase"]


async def get_eth_price(exchange_id: str) -> float:
    """Get ETH/USDT price from a specific exchange."""
    try:
        exchange = getattr(ccxt, exchange_id)()
        ticker = await exchange.fetch_ticker("ETH/USDT")
        await exchange.close()
        return float(ticker["last"])
    except Exception as e:
        print(f"Error fetching price from {exchange_id}: {str(e)}")
        return None


async def get_all_prices() -> Dict[str, float]:
    """Get ETH/USDT prices from all supported exchanges."""
    prices = {}
    for exchange_id in SUPPORTED_EXCHANGES:
        price = await get_eth_price(exchange_id)
        if price is not None:
            prices[exchange_id] = price
    return prices
