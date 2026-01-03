import re
import sys
from random import triangular, vonmisesvariate
from typing import List

sys.path.append("..")
from leetcode_75.util import (  # type: ignore
    debug_print,
    display_test_case,
    set_flag_debug,
)


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        triplets = []

        nums = sorted(nums)
        print(f"sorted> {nums}")

        for i in range(l):

        print(f"\n{triplets=}")

        return []


test_cases = [
    # ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
    ([0, 1, 1], []),
    # ([0, 0, 0], [[0, 0, 0]]),
]

s = Solution()

set_flag_debug(False)

for index, (test_case, expected) in enumerate(test_cases):
    # display_test_case(test_case, expected, index + 1)

    output = s.threeSum(test_case)
    # print("got:", output)
    passed = output == expected
    # print("Result  :", "✅ Pass" if passed else "❌ Fail")
