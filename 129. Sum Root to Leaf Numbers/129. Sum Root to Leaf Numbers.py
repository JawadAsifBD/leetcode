# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def sumToLeaf(node: Optional[TreeNode], total: int) -> int:
            total = total*10 + node.val
            if node.left is None and node.right is None:
                return total
            else:
                lefttotal = rightotal = 0
                if node.left is not None:
                    lefttotal = sumToLeaf(node.left, total)
                if node.right is not None:
                    rightotal = sumToLeaf(node.right, total)
                return lefttotal + rightotal

        if root is None:
            return 0
        else:
            return sumToLeaf(root, 0)
