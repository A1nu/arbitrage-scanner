import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

import unittest  # noqa: E402
from typing import Dict, Union, cast  # noqa: E402

from arbitrage import compare_prices  # noqa: E402


class TestArbitrage(unittest.TestCase):
    def test_no_arbitrage_small_spread(self) -> None:
        """Test that small spreads don't trigger arbitrage"""
        result = compare_prices("Exchange1", 1000.0, "Exchange2", 1000.5)
        self.assertIsNone(result)

    def test_arbitrage_opportunity(self) -> None:
        """Test that spreads above threshold trigger arbitrage detection"""
        result = compare_prices("Exchange1", 1000.0, "Exchange2", 1010.0)
        self.assertIsNotNone(result)
        result_dict = cast(Dict[str, Union[float, str]], result)
        self.assertEqual(result_dict["spread"], 1.0)  # 1% spread
        self.assertEqual(result_dict["price_a"], 1000.0)
        self.assertEqual(result_dict["price_b"], 1010.0)
        self.assertEqual(result_dict["action"], "BUY on Exchange1, SELL on Exchange2")

    def test_zero_prices(self) -> None:
        """Test that zero prices return None"""
        result = compare_prices("Exchange1", 0, "Exchange2", 1000.0)
        self.assertIsNone(result)
        result = compare_prices("Exchange1", 1000.0, "Exchange2", 0)
        self.assertIsNone(result)

    def test_custom_threshold(self) -> None:
        """Test with custom threshold"""
        # Should not trigger with default threshold
        result = compare_prices("Exchange1", 1000.0, "Exchange2", 1000.3)
        self.assertIsNone(result)

        # Should trigger with lower threshold
        result = compare_prices("Exchange1", 1000.0, "Exchange2", 1000.3, threshold=0.0001)
        self.assertIsNotNone(result)
        result_dict = cast(Dict[str, Union[float, str]], result)
        self.assertEqual(result_dict["spread"], 0.03)  # 0.03% spread

    def test_reverse_arbitrage(self) -> None:
        """Test arbitrage detection in both directions"""
        # Test when Exchange2 has lower price
        result = compare_prices("Exchange1", 1010.0, "Exchange2", 1000.0)
        self.assertIsNotNone(result)
        result_dict = cast(Dict[str, Union[float, str]], result)
        self.assertAlmostEqual(float(result_dict["spread"]), 0.99, places=2)  # 0.99% spread
        self.assertEqual(result_dict["action"], "BUY on Exchange2, SELL on Exchange1")


if __name__ == "__main__":
    unittest.main()
