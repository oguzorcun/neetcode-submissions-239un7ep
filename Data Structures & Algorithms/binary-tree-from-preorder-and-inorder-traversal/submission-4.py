# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # this is important to picture and internalize 
        # (yeap, duuuh, you know that order, but think in sub-tree terms)

        # preorder: [ root | ...left subtree nodes... | ...right subtree nodes... ]  
        # inorder:  [ ...left subtree nodes... | root | ...right subtree nodes... ]   

        inorder_node_indices = {}

        for i, n in enumerate(inorder):
            inorder_node_indices[n] = i

        def build(l: int, r: int, root_node_index_preorder: int) -> Optional[TreeNode]:
            # exit condition
            if l > r:
                return None

            # find root in inorder
            root_node = preorder[root_node_index_preorder]
            root_node_index_inorder = inorder_node_indices[root_node]

            # recurse
            # [l, r] is the current subtree inorder, root_node_index_inorder pointing to root of current subtree.
            # now I will recurse down to left and right subtrees of the current subtree
            
            left_sub = build(
                l, 
                root_node_index_inorder - 1, 
                root_node_index_preorder + 1 # bc, preorder is node,left,right so +1 lands on root of left subtree
            )

            number_of_nodes_in_left_subtree_of_current_subtree = root_node_index_inorder - l

            right_sub = build(
                root_node_index_inorder + 1, 
                r, 
                root_node_index_preorder + number_of_nodes_in_left_subtree_of_current_subtree + 1 
                # bc, preorder is node,left,right so gotta skip over all the left subtree to land on root of right subtree
                # so, i need the number of nodes in the left subtree which (root_node_index_inorder - l) gives me bc [l,r] range is the current inorder traersal. +1 is for the root of current subtree.
            )

            return TreeNode(root_node, left_sub, right_sub)

        return build(0, len(inorder) - 1, 0)

        
