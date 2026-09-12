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

    public boolean validate(TreeNode node, Integer min, Integer max) {
        if (node == null) return true;

        if ((max != null && node.val >= max) 
            || (min != null && node.val <= min)) return false;

        return validate(node.left, min, node.val) && validate(node.right, node.val, max);
    }

    public boolean isValidBST(TreeNode root) {
        return validate(root, null, null);
    }
}
