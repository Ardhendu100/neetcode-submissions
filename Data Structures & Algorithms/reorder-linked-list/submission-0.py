# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        slow = head
        fast = head

        # Let's find the middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        middle = slow

        # Reverse the second half

        curr = middle.next
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        middle.next = None

        second = prev
        
        # Now merge them
        first = head

        while second:
           next_first = first.next
           next_second = second.next

           first.next = second
           second.next = next_first

           first = next_first
           second = next_second