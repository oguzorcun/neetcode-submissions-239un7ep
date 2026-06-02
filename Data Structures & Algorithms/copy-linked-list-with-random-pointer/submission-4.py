"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur = head
        orig_to_copy = {None: None}

        while cur: 
            copy = Node(cur.val)
            orig_to_copy[cur] = copy
            cur = cur.next

        cur, copy = head, orig_to_copy[head]
        
        while cur: 
            copy.next = orig_to_copy[cur.next]
            copy.random = orig_to_copy[cur.random]
            cur, copy = cur.next, copy.next

        return orig_to_copy[head]   