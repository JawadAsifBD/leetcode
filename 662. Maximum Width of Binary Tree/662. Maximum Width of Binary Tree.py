# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findHeightWidth(self, node, height, width):
        if node:
            self.first_col_idx.setdefault(height, width)
            self.max_width = max(self.max_width, width-self.first_col_idx[height]+1)
            self.findHeightWidth(node.left, height+1, 2*width)
            self.findHeightWidth(node.right,height+1, 2*width+1)
        

    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.first_col_idx = {}
        self.max_width = 0
        
        self.findHeightWidth(root, 0, 0)
        return self.max_width