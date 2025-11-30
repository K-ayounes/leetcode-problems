import re
import sys
from collections import defaultdict
from multiprocessing import Value
from weakref import ref

from typing_extensions import List, Required

sys.path.append("..")
from leetcode_75.util import (  # type: ignore
    debug_print,
    display_test_case,
    set_flag_debug,
)


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        wt = len(t)
        ws = len(s)

        if wt > ws:
            return ""

        freq_t = defaultdict(int)
        for ct in t:
            freq_t[ct] += 1

        freq_s = defaultdict(int)
        for cs in s:
            freq_s[cs] += 1

        for freq_ct in freq_t.keys():
            if (freq_ct not in freq_s) or (freq_s[freq_ct] < freq_t[freq_ct]):
                # print(f"Mising character {freq_ct}")
                return ""

        if ws == wt:
            if freq_t == freq_s:
                return s

        ####
        map = defaultdict(list)
        start = None
        for i, c_s in enumerate(s):
            if c_s in freq_t:
                map[c_s].append(i)
                if start == None:
                    start = i
        if start is None:
            start = 0
        # print(map)
        # print(f"{start=}")
        matched = 0
        required = len(freq_t.keys())

        l = start
        r = start
        freq_w = defaultdict(int)

        jump = 0

        min_l = ws
        min_sub = slice(0, 0)

        while r < ws:
            char_r = s[r]

            # Update frequency if char is relevant
            if char_r in freq_t and matched != required:
                freq_w[char_r] += 1
                if freq_w[char_r] == freq_t[char_r]:
                    matched += 1

            # When window becomes valid
            if matched == required:
                msgs = [f"Window valid {s[l : r + 1]}"]

                curr_window_len = r - l + 1
                if curr_window_len <= min_l:
                    msgs.append(f"new min window of size {curr_window_len}")
                    min_sub = slice(l, r + 1)
                    min_l = curr_window_len

                # Shrink from left
                char_l = s[l]
                freq_w[char_l] -= 1
                if freq_w[char_l] < freq_t[char_l]:
                    matched -= 1
                msgs.append(f"dec.freq of {char_l}, {dict(freq_w)}")

                l += 1
                # Skip irrelevant chars while shrinking
                while l < ws - 1 and s[l] not in freq_t:
                    l += 1

                msgs.append(f"new window {s[l : r + 1]}")
                print("\t".join(msgs))

            # Expand only when invalid
            if matched != required:
                r += 1

        return s[min_sub]


test_cases = [
    (("cabefgecdaecf", "cae"), "aec"),
    (("ab", "a"), "a"),
    (("ab", "b"), "b"),
    (("AXXXABCAA", "AAC"), "CAA"),
    (("DADOBECODEBANC", "ABC"), "BANC"),  # normal case
    (
        ("ABAAC", "ABC"),
        "BAAC",
    ),  # special normal case where the correct answer contains duplicate AA
    (("ABC", "ABD"), ""),  # early return: D in t but not in S
    (("a", "a"), "a"),
    (("a", "aa"), ""),
]

s = Solution()

set_flag_debug(False)

for index, (test_case, expected) in enumerate(test_cases):
    display_test_case(test_case, expected, index + 1)

    output = s.minWindow(*test_case)
    print("got:", output)
    passed = (output) == (expected)
    print("Result  :", "✅ Pass" if passed else "📛 Fail")
