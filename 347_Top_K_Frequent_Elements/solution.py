import sys
from collections import defaultdict
from typing import List  # type: ignore

sys.path.append("..")
from leetcode_75.util import display_test_case  # type: ignore


class Solution:
    """
    Approach

    bucket sorting

    create an arrray of buckets (empty arrays), the number of buckets is based on the max frequency possible.
    Which is based on the length of the nums array.

    calcualte frequency and populate buckets.
    then loop backwards from end of buckets and return most frequent k.
    """

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        max_freq = len(nums)

        if max_freq == 0:
            return nums

        buckets = [[] for _ in range(max_freq + 1)]
        print("buckets")
        print(buckets)
        freqs = defaultdict(int)

        for number in nums:
            freqs[number] += 1

        print("freqs")
        print(freqs)
        for number, freq in freqs.items():
            print(number, freq)
            buckets[freq].append(number)

        most_k = []
        for i in range(len(buckets) - 1, 0, -1):
            bucket = buckets[i]

            for num in bucket:
                if k > 0:
                    most_k.append(num)
                    k -= 1

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

for index, (test_case, answer) in enumerate(test_cases):
    suggestion = s.topKFrequent(*test_case)
    display_test_case(test_case, answer, suggestion, index + 1)
