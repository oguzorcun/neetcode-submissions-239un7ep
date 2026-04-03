# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        
        if len(preorder) == 1:
            return TreeNode(preorder[0])

        root: Optional[TreeNode] = None

        inorder_node_indices = {}

        for i, n in enumerate(inorder):
            inorder_node_indices[n] = i

        def build(l: int, r: int, preorder_it: int) -> Optional[TreeNode]:
            # exit condition
            if l > r:
                return None

            # find root in inorder
            root_node = preorder[preorder_it]
            root_node_index_inorder = inorder_node_indices[root_node]

            # recurse
            left_sub = build(l, root_node_index_inorder - 1, preorder_it + 1)
            right_sub = build(root_node_index_inorder + 1, r , preorder_it + root_node_index_inorder - l + 1)

            return TreeNode(root_node, left_sub, right_sub)

        return build(0, len(inorder) - 1, 0)

        
