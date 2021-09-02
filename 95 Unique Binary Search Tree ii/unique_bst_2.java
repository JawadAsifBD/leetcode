/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<TreeNode> generateTrees(int n) {
        return rec(1,n);
    }
    
    public List<TreeNode> rec(int start, int end) {
        List<TreeNode> res = new ArrayList();
        if ( start > end ) {
            res.add(null);
            return res;
        }
        for(int i=start; i<=end; i++) {
            List<TreeNode> left = rec(start,i-1);
            List<TreeNode> right = rec(i+1,end);
            
            for(TreeNode l : left ) {
                for(TreeNode r : right ) {
                    TreeNode current = new TreeNode(i);
                    current.left = l;
                    current.right = r;
                    res.add(current);
                }
            }
        }
        return res;
    }
}