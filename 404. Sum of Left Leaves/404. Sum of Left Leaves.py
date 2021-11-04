# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        def sumsOfLeft(node: Optional[TreeNode], parent: Optional[TreeNode]) -> int:
            # check if current node is leaf

            if node.left is None and node.right is None:
                # check if current node is left child
                if parent is not None and parent.left == node:
                    return node.val
                else:
                    return 0
            else:
                leftsum = rightsum = 0
                if node.left is not None:
                    leftsum = sumsOfLeft(node.left, node)
                if node.right is not None:
                    rightsum = sumsOfLeft(node.right, node)
                return leftsum + rightsum

        if root is None:
            return 0
        else:
            return sumsOfLeft(root, None)
