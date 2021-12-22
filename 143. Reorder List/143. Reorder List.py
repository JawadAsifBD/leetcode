# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        res = Deque()
        cur = head
        while cur:
            res.append(cur)
            cur = cur.next

        prev = None
        while len(res) >= 2:
            h = res.popleft()
            t = res.pop()

            if prev:
                prev.next = h
            h.next = t
            prev = t

        if len(res) > 0:
            h = res.pop()
            if prev:
                prev.next = h
                prev = h
        if prev:
            prev.next = None
