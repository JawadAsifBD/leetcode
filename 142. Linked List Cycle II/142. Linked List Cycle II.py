from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = []
        t = head
        while t:
            if t in seen:
                return t
            else:
                seen.append(t)
            t = t.next
        return None
