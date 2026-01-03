import sys

sys.path.append("..")
from leetcode_75.util import (  # type: ignore
    debug_print,
    display_test_case,
    set_flag_debug,
)


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        l = 0
        r = 1
        w = len(s)
        ss = {s[0]}
        max_l = 0

        while r < w:
            head = s[r]

            while head in ss:
                ss.remove(s[l])
                l += 1

            r += 1
            ss.add(head)
            max_l = max(max_l, len(ss))
            print(s[l:r], ss)
        return max_l


test_cases = [
    ("abcabcbb", 3),
    ("bbbb", 1),
    ("pwwkew", 3),
    ("", 0),
    ("dvdf", 3),
    ("dvabcdf", 6),
    (" ", 1),
    ("dvddf", 2),
]

s = Solution()

set_flag_debug(False)

for index, (test_case, expected) in enumerate(test_cases):
    display_test_case(test_case, expected, index + 1)

    output = s.lengthOfLongestSubstring(test_case)
    print("got:", output)
    passed = (output) == (expected)
    print("Result  :", "✅ Pass" if passed else "📛 Fail")
