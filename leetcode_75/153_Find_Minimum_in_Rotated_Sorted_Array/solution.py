import sys
from typing import List

sys.path.append("..")
from leetcode_75.util import (  # type: ignore
    debug_print,
    display_test_case,
    set_flag_debug,
)


class Solution:
    def findMin(self, nums: List[int]) -> int:
        w = len(nums)

        if w == 1:
            return nums[0]

        l = 0
        r = w - 1
        m = r // 2

        while l < r:
            m = (r + l) // 2

            nums_m = nums[m]
            nums_r = nums[r]

            if nums_m > nums_r:  # min on right (pivot must be on the right)
                l = m + 1
            else:
                r = m

        return nums[l]


test_cases = [
    ([10, 20, 30, 40, 50], 10),
    ([50, 10, 20, 30, 40], 10),
    ([40, 50, 10, 20, 30], 10),
    ([30, 40, 50, 10, 20], 10),
    ([20, 30, 40, 50, 10], 10),
    ([10, 20, 30, 40, 50], 10),
    ([1, 2], 1),
    ([2, 1], 1),
    ([3, 4, 5, 1, 2], 1),
    ([4, 5, 6, 7, 0, 1, 2], 0),
    ([6, 7, 8, 9, 1, 2, 3, 4, 5], 1),
    ([5, 6, 7, 0, 1, 2, 3, 4], 0),
]

s = Solution()

set_flag_debug(False)

for index, (test_case, expected) in enumerate(test_cases):
    display_test_case(test_case, expected, index + 1)

    output = s.findMin(test_case)
    print("got:", output)
    passed = (output) == (expected)
    print("Result  :", "✅ Pass" if passed else "📛 Fail")
