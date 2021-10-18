# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        d1, p1 = depthAndParent(root, x, -1, -1)
        d2, p2 = depthAndParent(root, y, -1, -1)

        if d1 == d2 and p1 != p2:
            return True
        else:
            return False


def depthAndParent(node: Optional[TreeNode], x: int, parent: int, depth: int):
    if node.val == x:
        return depth, parent
    else:
        d = -1
        p = -1
        if node.left is not None:
            d, p = depthAndParent(node.left, x, node.val, depth+1)
            if d != -1:
                return d, p
        if node.right is not None:
            d, p = depthAndParent(node.right, x, node.val, depth+1)
        return d, p
