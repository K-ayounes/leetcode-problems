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
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head1 = list1
        head2 = list2
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        sortedHead = ListNode()
        pointer = sortedHead

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                pointer.next = list1
                list1 = list1.next
            else:
                pointer.next = list2
                list2 = list2.next

            pointer = pointer.next

        if list1 is not None:
            pointer.next = list1
        else:
            pointer.next = list2

        return sortedHead.next


test_cases = [
    (
        (
            [
                ListNode(2, ListNode(2, ListNode(4))),
                ListNode(1, ListNode(3, ListNode(3, ListNode(3, ListNode(5))))),
            ],
            ListNode(
                1,
                ListNode(
                    2,
                    ListNode(
                        2,
                        ListNode(3, ListNode(3, ListNode(3, ListNode(4, ListNode(5))))),
                    ),
                ),
            ),
        )
    )
]

s = Solution()

set_flag_debug(False)

for index, (test_case, expected) in enumerate(test_cases):
    display_test_case(list(map(lambda x: x.__str__(), test_case)), expected, index + 1)

    output = s.mergeTwoLists(*test_case)
    print("got:\n\t", output)
    passed = (output) == (expected)
    print("Result  :", "✅ Pass" if passed else "📛 Fail")
