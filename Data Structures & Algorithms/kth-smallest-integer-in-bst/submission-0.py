# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        s = []
        cur = root
        asc = []

        while s or cur:
            while cur:
                s.append(cur)
                cur = cur.left
            
            cur = s.pop()

            asc.append(cur.val)
            
            cur = cur.right

        return asc[k-1]