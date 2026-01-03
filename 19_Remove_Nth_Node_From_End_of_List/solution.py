import sys
from typing import Optional

from typing_extensions import List

sys.path.append("..")
from leetcode_75.util import (  # type: ignore
    debug_print,
    display_test_case,
    set_flag_debug,
)


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        if not isinstance(other, ListNode):
            return False

        a, b = self, other
        while a is not None and b is not None:
            if a.val != b.val:
                return False
            a = a.next
            b = b.next

        return a is None and b is None

    def __str__(self) -> str:
        p = self
        parts = []
        while p is not None:
            parts.append(f"[{p.val}]")
            p = p.next
        parts.append("None")
        return " -> ".join(parts)


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        behind = ListNode(-1, head)
        ahead = head

        while n:
            ahead = ahead.next
            n -= 1

        print(ahead)
        while ahead:
            ahead = ahead.next
            behind = behind.next

        print("behind:", behind)

        if behind.next == head:
            head = head.next
        else:
            rem = behind.next
            behind.next = behind.next.next
            del rem

        print(head)

        return head


test_cases = [
    (
        (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 1),
        ListNode(1, ListNode(2, ListNode(3, ListNode(5)))),
    ),
    (
        (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2),
        ListNode(1, ListNode(2, ListNode(3, ListNode(5)))),
    ),
    (
        (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 5),
        ListNode(1, ListNode(2, ListNode(3, ListNode(5)))),
    ),
    # (
    #     (
    #         ListNode(
    #             1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))
    #         ),
    #         2,
    #     ),
    #     ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(6))))),
    # ),
    # (
    #     (ListNode(1), 1),
    #     ListNode(),
    # ),
    # (
    #     (ListNode(1, ListNode(2)), 1),
    #     ListNode(2),
    # ),
]

s = Solution()

set_flag_debug(False)

for index, (test_case, expected) in enumerate(test_cases):
    display_test_case(list(map(lambda x: x.__str__(), test_case)), expected, index + 1)

    output = s.removeNthFromEnd(*test_case)
    # print("got:\n\t", output)
    passed = (output) == (expected)
    # print("Result  :", "✅ Pass" if passed else "📛 Fail")
