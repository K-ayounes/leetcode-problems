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
    def reorderList(self, head: Optional[ListNode]) -> None:
        left = head
        mid = head
        right = head

        while right is not None and right.next is not None:
            mid = mid.next
            right = right.next.next

        _nextMid = mid.next
        mid.next = None
        mid = _nextMid

        # reverse
        _prev = None

        while mid is not None:
            _next = mid.next
            mid.next = _prev
            _prev = mid
            mid = _next

        print(_prev)
        print(left)

        print("\nstart\n")

        while _prev is not None and left is not None:
            _nextLeft = left.next
            _nextRight = _prev.next
            print("!")
            print("left:", left)
            print()
            print("right:", _prev)
            print()
            print("_nextLeft:", _nextLeft)
            print()
            print("_nextRight:", _nextRight)
            print("?")
            left.next = _prev
            _prev.next = _nextLeft
            _prev = _nextRight
            left = _nextLeft
            print("3")
            print()
            print()

        print(head)
        return head

    def toStrg(self, head):
        nodes = []

        while head:
            nodes.append(f"[{head.val}]")
            head = head.next

        nodes.append("None")
        return " -> ".join(nodes)

    def toStrgP(self, head, pntrs):
        nodes = []

        while head:
            if head in pntrs:
                nodes.append(f"[{head.val}, 'X']")
            else:
                nodes.append(f"[{head.val}]")
            head = head.next

        if None in pntrs:
            nodes.append("(None, X)")
        else:
            nodes.append("None")

        return " -> ".join(nodes)


test_cases = [
    (
        ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))),
        ListNode(1, ListNode(5, ListNode(2, ListNode(4, ListNode(3))))),
    ),
    (
        ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))),
        ListNode(1, ListNode(6, ListNode(2, ListNode(5, ListNode(3, ListNode(4)))))),
    ),
]

s = Solution()

set_flag_debug(False)

for index, (test_case, expected) in enumerate(test_cases):
    display_test_case(test_case.__str__(), expected, index + 1)

    output = s.reorderList(test_case)
    print("got:\n\t", output)
    passed = (output) == (expected)
    print("Result  :", "✅ Pass" if passed else "📛 Fail")
