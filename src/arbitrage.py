from typing import Dict, Optional, Union


def compare_prices(
    name_a: str, price_a: float, name_b: str, price_b: float, threshold: float = 0.001
) -> Optional[Dict[str, Union[float, str]]]:
    """
    Compare prices between two sources. If spread exceeds threshold, return arbitrage info.
    """
    if price_a == 0 or price_b == 0:
        return None

    diff = price_b - price_a
    spread = diff / price_a

    if abs(spread) >= threshold:
        direction = (
            "BUY on %s, SELL on %s" % (name_a, name_b)
            if spread > 0
            else "BUY on %s, SELL on %s" % (name_b, name_a)
        )
        return {
            "spread": round(abs(spread) * 100, 3),
            "price_a": price_a,
            "price_b": price_b,
            "action": direction,
        }

    return None
