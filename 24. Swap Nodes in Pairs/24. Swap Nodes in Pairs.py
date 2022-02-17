# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        res = []
        t = head
        # populate list
        while t:
            res.append(t)
            t = t.next

        # swap
        for i in range(0, len(res)-1, 2):
            res[i], res[i+1] = res[i+1], res[i]

        # update pointer
        for i in range(len(res)-1):
            res[i].next = res[i+1]
        res[-1].next = None

        return res[0]
