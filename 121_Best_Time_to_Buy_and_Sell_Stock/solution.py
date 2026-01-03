import sys
from sqlite3.dbapi2 import Date
from typing import List

sys.path.append("..")
from leetcode_75.util import (  # type: ignore
    debug_print,
    display_test_case,
    set_flag_debug,
)


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_d = 0
        sell_d = 1
        max_profit = 0

        while sell_d < len(prices):
            buy = prices[buy_d]
            sell = prices[sell_d]
            print(",".join([str(p) for p in prices]), f"({buy_d},{sell_d})")
            print(f"{' ' * (buy_d * 2)}b{' ' * ((sell_d - buy_d) * 2 - 1)}s")

            if sell <= buy:
                buy_d = sell_d
                sell_d = buy_d + 1
            else:
                sell_d += 1
                max_profit = max(max_profit, sell - buy)

        return max_profit


test_cases = [
    ([7, 1, 5, 3, 6, 4], 5),
    ([7, 2, 5, 3, 6, 4, 1, 3], 4),
    ([7, 1], 0),
    ([2, 1, 2, 1, 0, 1, 2], 2),
]

s = Solution()

set_flag_debug(False)

for index, (test_case, expected) in enumerate(test_cases):
    display_test_case(test_case, expected, index + 1)

    output = s.maxProfit(test_case)
    print("got:", output)
    passed = (output) == (expected)
    print("Result  :", "✅ Pass" if passed else "❌ Fail")
