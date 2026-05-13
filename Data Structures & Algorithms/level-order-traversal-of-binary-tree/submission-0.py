# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        q = deque([(root, 0)])
        t = []

        while q:
            nodes = []
            level = q[0][1]
            while q and q[0][1] == level: 
                node = q.popleft()[0]
                nodes.append(node.val)
                if node.left: q.append((node.left, level + 1))
                if node.right: q.append((node.right, level + 1))
            t.append(nodes)
        return t