# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:

        def traverse_tree(node, depth=0):
            if not node:
                return
            depth_map[depth].append(node)
            traverse_tree(node.left, depth+1)
            traverse_tree(node.right, depth+1)

        depth_map = collections.defaultdict(list)
        traverse_tree(root)
        deepest_leaves_sum = sum(
            node.val for node in depth_map[max(depth_map.keys())])
        return deepest_leaves_sum
