# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead = None
        # loop over the main list
        while head is not None:

            # iterate sorted list
            curr = newHead
            prev = None
            while curr is not None:
                if curr.val > head.val:
                    t = ListNode(head.val, curr)
                    if prev is None:
                        # first element
                        newHead = t
                    else:
                        prev.next = t
                    break
                prev = curr
                curr = curr.next
            else:
                # did not encounter 'break' statement
                # i.e., either sorted List is empty or reached the end of sorted List
                if newHead is None:
                    # sorted list empty
                    newHead = ListNode(head.val, None)
                else:
                    # reached the end of sorted list
                    t = ListNode(head.val, None)
                    prev.next = t
            head = head.next
        return newHead
