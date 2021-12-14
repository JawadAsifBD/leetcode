# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def getSum(root: Optional[TreeNode]) -> int:
            nonlocal low
            nonlocal high
            res = 0
            if root is None:
                return 0
            if root.left is not None:
                res += getSum(root.left)
            if root.right is not None:
                res += getSum(root.right)

            if root.val >= low and root.val <= high:
                res += root.val

            print(res)
            return res
        return getSum(root)
