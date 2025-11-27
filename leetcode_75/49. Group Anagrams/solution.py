import sys
from typing import List  # type: ignore

sys.path.append("..")
from leetcode_75.util import display_test_case  # type: ignore


class Solution:
    """
    Approach 1
    use frequency dict as hash
    """

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for string in strs:
            freq = self.get_frequency(string)
            hash_freq = frozenset(freq.items())

            if hash_freq in groups:
                groups[hash_freq].append(string)
            else:
                groups[hash_freq] = [string]

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
