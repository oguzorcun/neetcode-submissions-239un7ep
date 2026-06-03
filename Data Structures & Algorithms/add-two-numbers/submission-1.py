# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        elde = 0
        dum = cur = ListNode()

        while l1 or l2:
            digit1 = l1.val if l1 else 0
            digit2 = l2.val if l2 else 0
            sum_digits = digit1 + digit2 + elde
            elde = sum_digits // 10
            
            cur.next = ListNode(sum_digits % 10)
            cur = cur.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        if elde:
            cur.next = ListNode(elde)

        return dum.next
