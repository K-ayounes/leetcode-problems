import sys
from collections import defaultdict
from pickletools import stackslice
from tracemalloc import start
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
        map = {}
        path_l = {}

        for num in nums:
            next = num + 1
            prev = num - 1
            if num not in map:
                map[num] = None
                path_l[num] = 1

                if prev in map:
                    map[prev] = num
                    path_l[num] = path_l[prev] + 1

                if next in map:
                    map[num] = next
                    debug_print(next)
                    while next is not None:
                        debug_print(next - 1)
                        path_l[next] = path_l[next - 1] + 1
                        next = map[next]
                        debug_print(next)

            # debug_print(path_l)

        # debug_print(map)
        # debug_print(path_l)

        # debug_print(max(path_l.values()))
        return max(path_l.values())


test_cases = [
    ([100, 4, 200, 1, 3, 2], 4),
    ([0, 3, 7, 2, 5, 8, 1, 4, 6, 0], 9),
    ([0, -1], 2),
]

s = Solution()

set_flag_debug(True)

for index, (test_case, expected) in enumerate(test_cases):
    display_test_case(test_case, expected, index + 1)

    output = s.longestConsecutive(test_case)
    print("got:", output)
    passed = (output) == (expected)
    print("Result  :", "✅ Pass" if passed else "❌ Fail")
