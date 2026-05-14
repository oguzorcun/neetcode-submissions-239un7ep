# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.bst(root, float('-inf'), float('inf'))

    def bst(self, root: Optional[TreeNode], higher_than: float, lower_than: float) -> bool:
        if not root: return True
        if not higher_than < root.val < lower_than: return False

        return self.bst(root.left, higher_than, root.val) and self.bst(root.right, root.val, lower_than)
