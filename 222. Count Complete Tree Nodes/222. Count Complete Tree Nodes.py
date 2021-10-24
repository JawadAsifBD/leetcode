# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        count = getCount(root)
        return count


def getCount(node):
    if node is None:
        return 0
    c1 = getCount(node.left)
    c2 = getCount(node.right)
    return c1+c2+1
