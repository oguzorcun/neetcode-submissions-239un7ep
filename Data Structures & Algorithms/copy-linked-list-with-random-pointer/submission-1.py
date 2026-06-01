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
        if not head: return None
        cur = head.next
        copy = copy_head = Node(head.val)
        orig_to_copy = {head: copy_head}

        while cur: 
            copy.next = Node(cur.val)
            orig_to_copy[cur] = copy.next
            cur, copy = cur.next, copy.next

        cur, copy = head, copy_head

        while cur: 
            copy.random = orig_to_copy[cur.random] if cur.random else None
            cur, copy = cur.next, copy.next

        return copy_head