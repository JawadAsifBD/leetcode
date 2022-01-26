from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        res = []

        def BST_to_list(root: TreeNode) -> None:
            nonlocal res
            if root:
                res.append(root.val)
                BST_to_list(root.left)
                BST_to_list(root.right)
        BST_to_list(root1)
        BST_to_list(root2)
        res.sort()
        return res
