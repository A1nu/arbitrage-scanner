from typing import Dict, Optional

import ccxt

# List of exchanges to monitor
SUPPORTED_EXCHANGES = ["binance", "kucoin", "huobi", "okx", "bybit", "gateio", "kraken", "coinbase"]


async def get_eth_price(exchange_id: str) -> Optional[float]:
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


def get_binance_price() -> Optional[float]:
    try:
        exchange = ccxt.binance()
        ticker = exchange.fetch_ticker("ETH/USDT")
        return float(ticker["last"])
    except Exception:
        return None


def get_kucoin_price() -> Optional[float]:
    try:
        exchange = ccxt.kucoin()
        ticker = exchange.fetch_ticker("ETH/USDT")
        return float(ticker["last"])
    except Exception:
        return None


def get_huobi_price() -> Optional[float]:
    try:
        exchange = ccxt.huobi()
        ticker = exchange.fetch_ticker("ETH/USDT")
        return float(ticker["last"])
    except Exception:
        return None


def get_okx_price() -> Optional[float]:
    try:
        exchange = ccxt.okx()
        ticker = exchange.fetch_ticker("ETH/USDT")
        return float(ticker["last"])
    except Exception:
        return None


def get_bybit_price() -> Optional[float]:
    try:
        exchange = ccxt.bybit()
        ticker = exchange.fetch_ticker("ETH/USDT")
        return float(ticker["last"])
    except Exception:
        return None


def get_gateio_price() -> Optional[float]:
    try:
        exchange = ccxt.gateio()
        ticker = exchange.fetch_ticker("ETH/USDT")
        return float(ticker["last"])
    except Exception:
        return None


def get_kraken_price() -> Optional[float]:
    try:
        exchange = ccxt.kraken()
        ticker = exchange.fetch_ticker("ETH/USDT")
        return float(ticker["last"])
    except Exception:
        return None


def get_coinbase_price() -> Optional[float]:
    try:
        exchange = ccxt.coinbase()
        ticker = exchange.fetch_ticker("ETH/USDT")
        return float(ticker["last"])
    except Exception:
        return None
