# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        view = []
        h = 0
        q = deque([(root, 0)])

        while q:
            while q and q[0][1] == h: 
                node = q.popleft()[0]
                if node.left: q.append((node.left, h + 1))
                if node.right: q.append((node.right, h + 1))
            view.append(node.val)
            h += 1
        return view