# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        def get_child_tail(node: 'Node') -> 'Node':
            t = node
            prev = None
            while t is not None:
                if t.child is not None:
                    child_tail = get_child_tail(t.child)

                    te = t.next

                    t.next = t.child
                    t.child.prev = t

                    child_tail.next = te
                    if te is not None:
                        te.prev = child_tail
                    t.child = None
                prev = t
                t = t.next
            return prev

        if head is None:
            return None
        temp = head
        while temp is not None:
            if temp.child is not None:
                child_tail = get_child_tail(temp.child)

                t = temp.next

                temp.next = temp.child
                temp.child.prev = temp

                child_tail.next = t
                if t is not None:
                    t.prev = child_tail
                temp.child = None
            temp = temp.next
        return head
