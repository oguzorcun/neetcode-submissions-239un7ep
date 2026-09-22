# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # dum = ListNode(0, head)
        # curr, fast = dum, head
        
        # for _ in range(n): fast = fast.next
        # while fast:
        #     curr = curr.next
        #     fast = fast.next
        # curr.next = curr.next.next
        # return dum.next

        # find list length
        l, cur = 0, head
        while cur:
            l += 1
            cur = cur.next

        # means delete the 1st node     
        if l - n == 0: return head.next

        # find the node to be deleted
        cur = head
        for _ in range(l - n - 1):
            cur = cur.next
        
        cur.next = cur.next.next

        return head


