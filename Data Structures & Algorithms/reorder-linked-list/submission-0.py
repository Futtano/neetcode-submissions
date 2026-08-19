# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        right_half = self._split(head)
        end = self._reverse(right_half)

        start = head
        while(start.next):
            next = start.next
            start.next = end
            start = start.next
            end = next

    def _split(self, head: Optional[ListNode]) -> ListNode:
        fast = head

        while(fast and fast.next):
            head = head.next
            fast = fast.next.next

        return head

    def _reverse(self, head: Optional[ListNode]) -> ListNode:
        prev = None
        curr = head

        while(curr):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        return prev
