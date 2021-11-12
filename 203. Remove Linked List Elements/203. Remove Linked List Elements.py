# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr is not None:
            if curr.val == val:  # found a match
                if prev is not None:
                    # found at non-first element
                    prev.next = curr.next
                    curr = curr.next
                    # prev unchanged
                else:
                    # found at first element
                    head = curr.next
                    curr = curr.next
                    prev = None
            else:
                prev = curr
                curr = curr.next
        return head
