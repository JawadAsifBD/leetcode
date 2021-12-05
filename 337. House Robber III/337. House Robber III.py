# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def helper(node):
            # corner case
            if not node:
                return 0, 0
                # children node
            left_rub_child, left_notrub_child = helper(node.left)
            right_rub_child, right_notrub_child = helper(node.right)
            # current node
            rub_node = node.val + left_notrub_child + right_notrub_child
            not_rub_node = max(right_rub_child, right_notrub_child) + \
                max(left_rub_child, left_notrub_child)

            return rub_node, not_rub_node

        return max(helper(root))
