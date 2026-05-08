# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dum = ListNode(0, head)
        curr, fast = dum, head
        
        for _ in range(n): fast = fast.next
        while fast:
            curr = curr.next
            fast = fast.next
        curr.next = curr.next.next
        return dum.next