import sys
from collections import defaultdict

sys.path.append("..")
from leetcode_75.util import (  # type: ignore
    debug_print,
    display_test_case,
    set_flag_debug,
)


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) < 2:
            return len(s)

        l = 0
        r = 0
        w = len(s)
        curr_w = 1
        k2 = k
        max_w = 1
        freq = defaultdict(int)
        max_f = 1

        while r < w:
            freq[s[r]] += 1
            max_f = max(max_f, freq[s[r]])
            print(freq, max_f, r - l + 1 - max_f)

            if r - l + 1 - max_f > k:
                l += 1
            max_w = max(max_w, r - l + 1)
            r += 1
        return max_w


test_cases = [
    (("ABAB", 2), 4),
    (("ABAB", 1), 3),
    (("ABAB", 0), 1),
    (("ABAB", 0), 1),
    (("ABAB", 0), 1),
    (("ABAB", 0), 1),
    (("AABABBA", 1), 4),
    (("ABBB", 1), 4),
]

s = Solution()

set_flag_debug(False)

for index, (test_case, expected) in enumerate(test_cases):
    display_test_case(test_case, expected, index + 1)

    output = s.characterReplacement(*test_case)
    print("got:", output)
    passed = (output) == (expected)
    print("Result  :", "✅ Pass" if passed else "📛 Fail")
