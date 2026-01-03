import sys
from typing import List  # type: ignore

sys.path.append("..")
from leetcode_75.util import display_test_case  # type: ignore


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for string in strs:
            count = [0] * 26
            for c in string:
                count[ord(c) - ord("a")] += 1
            hash = tuple(count)
            if hash in groups:
                groups[hash].append(string)
            else:
                groups[hash] = [string]

        return list(groups.values())

    def get_frequency(self, string):
        freq = {}
        for char in string:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        return freq


test_cases = [
    (
        (["eat", "tea", "tan", "ate", "nat", "bat"]),
        [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
    ),
    (([""]), [[""]]),
    ((["a"]), [["a"]]),
]

s = Solution()

for index, (test_case, answer) in enumerate(test_cases):
    suggestion = s.groupAnagrams(test_case)
    display_test_case(test_case, answer, suggestion, index + 1)
