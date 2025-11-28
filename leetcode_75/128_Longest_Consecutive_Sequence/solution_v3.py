import sys
from typing import List

sys.path.append("..")
from leetcode_75.util import (  # type: ignore
    debug_print,
    display_test_case,
    set_flag_debug,
)


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        lookup = set(nums)

        max_len = 1
        while len(lookup):
            num = lookup.pop()
            if num - 1 not in lookup:
                c_len = 1
                while (num + 1) in lookup:
                    num += 1
                    c_len += 1
                    lookup.remove(num)

                max_len = max(c_len, max_len)
            else:
                lookup.add(
                    num
                )  ## this can cause infinite loops since the pop-add cycle does not guarantee a new number each time.

        return max_len


test_cases = [
    ([100, 4, 200, 1, 2, 3], 4),
    ([0, 3, 7, 2, 5, 8, 1, 4, 6], 9),
    ([0, -1], 2),
    ([0, 1, -1], 3),
    ([1, 0, -1], 3),
    ([0, -1, 1], 3),
    ([7, -9, 3, -6, 3, 5, 3, 6, -2, -5, 8, 6, -4, -6, -4, -4, 5, -9, 2, 7, 0, 0], 4),
    ([-6, 8, -5, 7, -9, -1, -7, -6, -9, -7, 5, 7, -1, -8, -8, -2, 0], 5),
]

s = Solution()

set_flag_debug(True)

for index, (test_case, expected) in enumerate(test_cases):
    display_test_case(test_case, expected, index + 1)
    output = s.longestConsecutive(test_case)
    print("got:", output)
    passed = (output) == (expected)
    print("Result  :", "✅ Pass" if passed else "❌ Fail")
