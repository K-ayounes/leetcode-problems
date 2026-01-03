import sys
from string import printable
from typing import List  # type: ignore

sys.path.append("..")
from leetcode_75.util import (  # type: ignore
    debug_print,
    display_test_case,
    set_flag_debug,
)


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)

        answer = [1] * l

        prefix = [1] * l
        suffix = [1] * l
        prefix[0] = nums[0]
        suffix[-1] = nums[-1]

        for i in range(1, l):
            prefix[i] = nums[i] * prefix[i - 1]
        for i in range(l - 2, -1, -1):
            suffix[i] = nums[i] * suffix[i + 1]

        for i in range(1, l):
            answer[i] *= prefix[i - 1]
            answer[i - 1] *= suffix[i]

        return answer


test_cases = [
    (
        [1, 2, 3, 4],
        [24, 12, 8, 6],
    ),
    ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
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
