# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        def preOrder(r: Optional[TreeNode]) -> str:
            if not r:
                return 'N'
            return ''.join([str(r.val), '|', preOrder(r.left), '|', preOrder(r.right)])

        return preOrder(root)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        preOrder = data.split('|')
        i = 0

        def build() -> Optional[TreeNode]:
            nonlocal i
            node = preOrder[i]
            i += 1
            if node == 'N':
                return None
            left = build()
            right = build()
            return TreeNode(int(node), left, right)
            
        return build()