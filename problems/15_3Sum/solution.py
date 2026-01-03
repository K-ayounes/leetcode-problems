import sys
from random import vonmisesvariate
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

        visited = set()
        values = {}
        answers = []

        for i in range(0, l):
            for j in range(i + 1, l):
                for k in range(j + 1, l):
                    i_data = nums[i]
                    j_data = nums[j]
                    k_data = nums[k]
                    sum = i_data + j_data + k_data
                    if sum == 0:
                        triplet = [i_data, j_data, k_data]
                        triplet_hash = tuple(sorted(triplet))
                        if triplet_hash not in visited:
                            visited.add(triplet_hash)
                            answers.append(triplet)

        return answers


test_cases = [
    ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
    ([0, 1, 1], []),
    ([0, 0, 0], [[0, 0, 0]]),
]

s = Solution()

set_flag_debug(False)

for index, (test_case, expected) in enumerate(test_cases):
    display_test_case(test_case, expected, index + 1)

    output = s.threeSum(test_case)
    print("got:", output)
    passed = output == expected
    print("Result  :", "✅ Pass" if passed else "❌ Fail")
