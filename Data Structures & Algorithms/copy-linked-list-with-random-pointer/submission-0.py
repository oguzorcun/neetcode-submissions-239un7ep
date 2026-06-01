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
        adr_index = {head: 0}
        random_index = []
        copy = copy_head = Node(head.val)
        copy_index_adr = [copy_head]

        i = 1
        while cur: 
            adr_index[cur] = i
            copy.next = Node(cur.val)
            cur, copy = cur.next, copy.next
            copy_index_adr.append(copy)
            i += 1
        
        cur = head
        while cur:
            if cur.random: random_index.append(adr_index[cur.random])
            else: random_index.append(-1)
            cur = cur.next
        
        i = 0
        copy = copy_head
        while copy:
            copy.random = None if random_index[i] == -1 else copy_index_adr[random_index[i]]
            copy = copy.next
            i += 1

        

        return copy_head