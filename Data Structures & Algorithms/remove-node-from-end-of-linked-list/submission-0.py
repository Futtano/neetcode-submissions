# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Time: O(N)
    # Space: O(1)
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = slow = head
        prev = None

        # Move fast forward N times
        for i in range(n):
            fast = fast.next

        # Move slow and fast until fast is None
        while (fast):
            prev = slow
            slow = slow.next
            fast = fast.next

        # if the node to remove is not the head of the list
        if prev:
            prev.next = slow.next
        else:
            head = slow.next

        return head


        