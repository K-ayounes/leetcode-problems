import sys
from string import printable
from typing import List  # type: ignore

sys.path.append("..")
from leetcode.util import debug_print, display_test_case, set_flag_debug  # type: ignore


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        debug_print(f"{prefix=}")
        debug_print(f"{suffix=}")

        return []


test_cases = [
    (
        # example: ([1,2,3,4], [24,12,8,6])
        [1, 2, 3, 4],
        [24, 12, 8, 6],
    )
]

s = Solution()

set_flag_debug(True)

for index, (test_case, expected) in enumerate(test_cases):
    display_test_case(test_case, expected, index + 1)

    # output placeholder
    output = s.productExceptSelf(test_case)  # Replace with actual call to solution
    print("got:", output)
    passed = set(output) == set(expected)
    print("Result  :", "✅ Pass" if passed else "❌ Fail")
