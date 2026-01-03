import sys
from pickle import TRUE
from sre_compile import FAILURE
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
            debug_msg = f"num {num} in map"
            if num not in map:
                debug_msg = f"{num=}"
                if prev in map:
                    if next in map:
                        debug_msg += f" # (1) has prev: {prev} and next: {next}"
                        if prev is not None:
                            prev_next = map[prev]
                            next_next = map[next]
                            debug_msg += f" # (1) has prev_next: {prev_next} and next_next: {next_next}"
                            if (prev_next is None) and (next_next is None):
                                debug_msg += f" # (1)"
                                map[prev] = next
                                map[next] = prev
                            elif prev_next is None:
                                debug_msg += f" # (2)"
                                map[prev] = next_next
                                map[next_next] = prev
                                del map[next]
                            elif next_next is None:
                                debug_msg += f" # (3)"
                                map[next] = prev_next
                                map[prev_next] = next
                                del map[prev]
                            else:
                                debug_msg += f" # (4)"
                                map[prev_next] = next_next
                                map[next_next] = prev_next
                                del map[prev]
                                del map[next]
                    else:  # has prev but no next
                        debug_msg += f" # (2) has prev: {prev} and NO next"
                        if map[prev] is None:
                            map[prev] = num
                            map[num] = prev
                        else:
                            # cycle
                            prev_next = map[prev]
                            map[prev_next] = num
                            map[num] = prev_next
                            del map[prev]

                elif next in map:
                    debug_msg += f" # (3) has next: {next} and NO prev"
                    next_next = map[next]
                    if next_next is not None:
                        map[num] = next_next
                        map[next_next] = num
                        del map[num]
                    else:
                        map[num] = next
                        map[next] = num
                else:
                    debug_msg += " # has NO prev AND NO next"
                    map[num] = None

            debug_print(debug_msg)
            debug_print(map)
            debug_print("\n")
        debug_print(map)

        result = max(abs(k - v) if v is not None else 0 for k, v in map.items()) + 1
        debug_print(result)
        return result


test_cases = [
    # ([100, 4, 200, 1, 2, 3], 4),
    # ([0, 3, 7, 2, 5, 8, 1, 4, 6], 9),
    # ([0, -1], 2),
    # ([0, 1, -1], 3),
    # ([1, 0, -1], 3),
    # ([0, -1, 1], 3),
    # ([7, -9, 3, -6, 3, 5, 3, 6, -2, -5, 8, 6, -4, -6, -4, -4, 5, -9, 2, 7, 0, 0], 4),
    ([-6, 8, -5, 7, -9, -1, -7, -6, -9, -7, 5, 7, -1, -8, -8, -2, 0], 5),
]

s = Solution()

set_flag_debug(True)

for index, (test_case, expected) in enumerate(test_cases):
    display_test_case(test_case, expected, index + 1)
    output = s.longestConsecutive(test_case)
    test_case.sort()
    debug_print(test_case)
    print("got:", output)
    passed = (output) == (expected)
    print("Result  :", "✅ Pass" if passed else "❌ Fail")
