import sys
from typing import List  # type: ignore

sys.path.append("..")
from leetcode_75.util import display_test_case  # type: ignore


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        solutions = {}

        for index, num in enumerate(nums):
            if num in solutions:
                return [index, solutions[num]]

            solutions[target - num] = index

        return [0]


test_cases = [
    (([2, 7, 11, 15], 9), [0, 1]),
    (([3, 2, 4], 6), [1, 2]),
    (([3, 3], 6), [0, 1]),
]
s = Solution()

for index, (test_case, answer) in enumerate(test_cases):
    suggestion = s.twoSum(*test_case)
    display_test_case(test_case, answer, suggestion, index + 1)
