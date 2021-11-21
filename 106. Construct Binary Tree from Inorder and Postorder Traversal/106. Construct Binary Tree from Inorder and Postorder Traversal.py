# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        pos = -1
        if inorder:
            pos = inorder.index(postorder[-1])
        if pos > -1:
            return TreeNode(postorder[-1],
                            self.buildTree(inorder[:pos], postorder[:pos]),
                            self.buildTree(inorder[pos+1:], postorder[pos:-1]))
        return None
