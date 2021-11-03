# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    res = 0

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def sumToLeaf(node: Optional[TreeNode], sum: int) -> int:
            if node is None:
                return sum
            leftsum = 0
            rightsum = 0
            if node.left is not None:
                leftsum = sumToLeaf(node.left, sum*10)
            if node.right is not None:
                rightsum = sumToLeaf(node.right, sum*10)
            sum = leftsum + rightsum
            return sum
