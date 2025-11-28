import sys

sys.path.append("..")
from leetcode_75.util import (  # type: ignore
    debug_print,
    display_test_case,
    set_flag_debug,
)


class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True
        left_p = 0
        right_p = len(s) - 1

        while left_p < right_p:
            left_d = s[left_p].lower()
            right_d = s[right_p].lower()

            if left_d.isalnum() and right_d.isalnum():
                if left_d != right_d:
                    return False
                left_p += 1
                right_p -= 1
            else:
                if not left_d.isalnum():
                    left_p += 1

                if not right_d.isalnum():
                    right_p -= 1

        return True


test_cases = [
    ("A man, a plan, a canal: Panama", True),
    ("race a car", False),
    (" ", True),
    (".,", True),
    (".a,", True),
    ("a.b,a", True),
]

s = Solution()

set_flag_debug(False)

for index, (test_case, expected) in enumerate(test_cases):
    display_test_case(test_case, expected, index + 1)

    output = s.isPalindrome(test_case)
    print("got:", output)

    passed = (output) == (expected)
    print("Result  :", "✅ Pass" if passed else "❌ Fail")
