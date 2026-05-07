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

        # find mid
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        mid = slow.next
        slow.next = None

        # reverse 2nd half
        tail = None
        while mid:
            nxt = mid.next
            mid.next = tail
            tail = mid
            mid = nxt

        print(head)
        print(tail)

        # wove
        curr = head

        while tail:
            tail_next = tail.next
            curr_next = curr.next

            curr.next = tail
            tail.next = curr_next

            tail = tail_next
            curr = curr_next
            








        

        