# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = TreeNode(val=val)
        if not root:
            return node
        temp = root
        prev = None
        while temp:
            prev = temp
            if val > temp.val:
                temp = temp.right
            else:
                temp = temp.left
        if val > prev.val:
            prev.right = node
        else:
            prev.left = node
        return root
