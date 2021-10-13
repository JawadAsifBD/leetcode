# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        for i in range(1, len(preorder)):
            setNode(root, preorder[i])
        return


def setNode(node: TreeNode, val: int):
    if node.val > val:
        if node.left is None:  # no left in the node
            newNode = TreeNode(val)
            node.left = newNode
            return
        else:
            setNode(node.left, val)
    else:
        if node.right is None:
            newNode = TreeNode(val)
            node.right = newNode
            return
        else:
            setNode(node.right, val)
