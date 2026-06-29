# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        l = 0
        
        while curr:
            l+=1
            curr = curr.next
        
        # remove head
        if l == n:
            return head.next

        # Find node before n
        p = l - n - 1
        curr = head

        for _ in range(p):
            curr = curr.next
        
        curr.next = curr.next.next

        return head

