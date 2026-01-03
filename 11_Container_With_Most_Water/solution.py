import sys
from typing import List

sys.path.append("..")
from leetcode_75.util import (  # type: ignore
    debug_print,
    display_test_case,
    set_flag_debug,
)


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        l = len(height)
        s = 0
        e = l - 1

        while e > s:
            height_s = height[s]
            height_e = height[e]

            area = (e - s) * min(height_s, height_e)
            max_area = max(max_area, area)

            if height_e > height_s:
                s += 1
            else:
                e -= 1

        return max_area


test_cases = [
    ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
    ([1, 1], 1),
    ((0, 0, 0, 0), 0),
    ([10, 3, 3, 1], 6),
]

s = Solution()

set_flag_debug(False)

for index, (test_case, expected) in enumerate(test_cases):
    display_test_case(test_case, expected, index + 1)

    output = s.maxArea(test_case)
    print("got:", output)
    passed = (output) == (expected)
    print("Result  :", "✅ Pass" if passed else "❌ Fail")
