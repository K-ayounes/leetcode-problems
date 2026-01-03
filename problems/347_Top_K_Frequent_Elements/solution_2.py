import sys
from collections import defaultdict
from typing import List  # type: ignore

sys.path.append("..")
from leetcode_75.util import display_test_case  # type: ignore


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:  # type: ignore
        freq_table = defaultdict(int)
        n = len(nums)

        if n == 1:
            return nums

        # Count frequencies
        for num in nums:
            freq_table[num] += 1

        # Bucket sort: index = frequency
        buckets = [[] for _ in range(n + 1)]
        for num, freq in freq_table.items():
            buckets[freq].append(num)

        # Collect top k frequent elements
        most_k = []
        for i in range(n, 0, -1):
            for num in buckets[i]:
                most_k.append(num)
                if len(most_k) == k:
                    return most_k


test_cases = [
    (
        ([1, 1, 1, 2, 2, 3], 2),
        [1, 2],
    ),
    (
        ([1], 1),
        [1],
    ),
    (
        ([1, 2, 1, 2, 1, 2, 3, 1, 3, 2], 2),
        [1, 2],
    ),
    (
        ([-1, -1], 1),
        [-1],
    ),
]

s = Solution()

for index, (test_case, expected) in enumerate(test_cases):
    display_test_case(test_case, expected, index + 1)
    output = s.topKFrequent(*test_case)
    print("got:", output)
    passed = set(output) == set(expected)
    print("Result  :", "✅ Pass" if passed else "❌ Fail")
