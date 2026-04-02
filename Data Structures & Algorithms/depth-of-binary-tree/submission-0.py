# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0

        q = deque([(root, 1)])
        max_d = 0

        while q:
            node, d = q.popleft()
            
            max_d = max(max_d, d)

            if node.left:
                q.append((node.left, d + 1))
            if node.right:
                q.append((node.right, d + 1))

        return max_d