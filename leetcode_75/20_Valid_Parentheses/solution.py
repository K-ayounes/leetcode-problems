import sys

sys.path.append("..")
from leetcode_75.util import (  # type: ignore
    debug_print,
    display_test_case,
    set_flag_debug,
)


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openers = {"{", "(", "["}
        closers = {"}": "{", ")": "(", "]": "["}

        for par in s:
            if par in openers:
                stack.append(par)
            elif par in closers:
                if len(stack) and stack[-1] == closers[par]:
                    stack.pop()
                else:
                    return False

        if len(stack):
            return False

        return True


test_cases = [
    ("()", True),
    ("(", False),
    (")", False),
    ("[]", True),
    ("[", False),
    ("]", False),
    ("{}", True),
    ("{", False),
    ("}", False),
    ("([{}])", True),
    ("(])", False),
    ("([)]", False),
    ("([)]", False),
]

s = Solution()

set_flag_debug(False)

for index, (test_case, expected) in enumerate(test_cases):
    display_test_case(test_case, expected, index + 1)

    output = s.isValid(test_case)
    print("got:", output)
    passed = (output) == (expected)
    print("Result  :", "✅ Pass" if passed else "📛 Fail")
