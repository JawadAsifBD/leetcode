# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.answer = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.findMaxLength(root)
        return self.answer

    def findMaxLength(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            leftlength = self.findMaxLength(root.left)
            rightlength = self.findMaxLength(root.right)
            self.answer = max(self.answer, leftlength+rightlength)
            return 1 + max(leftlength, rightlength)
