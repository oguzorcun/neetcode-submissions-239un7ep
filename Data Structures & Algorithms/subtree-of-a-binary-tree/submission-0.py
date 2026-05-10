# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSameTree(self, t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
        s = [(t1, t2)]
        while s:
            n1, n2 = s.pop()
            if not n1 and not n2: continue
            if not n1 or not n2: return False
            if n1.val != n2.val: return False

            s.append((n1.left, n2.left))
            s.append((n1.right, n2.right))
            
        return True 
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        s = [root]

        while s:
            node = s.pop()
            if node.val == subRoot.val and self.isSameTree(node, subRoot):
                return True
            if node.left: s.append(node.left)
            if node.right: s.append(node.right)
        
        return False

                

    

            