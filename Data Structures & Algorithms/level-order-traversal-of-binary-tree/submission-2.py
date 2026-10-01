# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        q = deque([root])
        t = []

        while q:
            nodes = []
            for _ in range(len(q)): 
                node = q.popleft()
                nodes.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            t.append(nodes)
        return t