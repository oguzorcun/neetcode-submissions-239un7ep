# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        nodes = []
        curr = self
        while curr:
            nodes.append(str(curr.val))
            curr = curr.next
        return " -> ".join(nodes)
    

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr, tail = head, None
        n = 0

        while curr:
            n += 1
            curr = curr.next
        if n <= 2: return
        curr = head
        for _ in range((n-1) // 2): curr = curr.next
        second_half = curr.next
        curr.next = None
        curr = second_half
        while curr:
            tmp = curr.next
            curr.next = tail
            tail = curr
            curr = tmp

        print(head)
        print(tail)

        dummy = head
        curr = head.next

        for i in range(n-1):
            if i % 2 == 0:
                dummy.next = tail
                tail = tail.next
            else:
                dummy.next = curr
                curr = curr.next
            dummy = dummy.next
        
        dummy.next = None
        

        