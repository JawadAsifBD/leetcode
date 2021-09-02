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
        List<TreeNode> res = rec(1,n);
        return res;
    }
    
    public List<TreeNode> rec(int start, int end) {
        List<TreeNode> res = new ArrayList<>();
        
        if(start > end) {
            return List.of(new TreeNode());
        }
        
        if (start == end) {
            return List.of(new TreeNode(start));
        }
        
        
        for(int i = start; i <= end; i++) {
            List<TreeNode> left = rec(start,i-1);
            List<TreeNode> right = rec(i+1,end);


            for( TreeNode l : left) {
                for (TreeNode r: right) {
                    res.add(new TreeNode(i,l,r));
                }
            }

        }
        return res;
    }
}