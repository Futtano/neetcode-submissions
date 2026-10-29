# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Time complexity: O(N)
    # Space complexity: O(1)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast is not None:
            # Fast moves two links per iteration
            fast = fast.next.next if fast and fast.next else None
            # Slow advances by one
            slow = slow.next if slow else None
            
            if slow and fast and slow is fast:
                # If the eventually meet, there is indeed a cycle
                # This check must be placed after the movement of
                # the two pointers if they both start at the same node
                # to ensure this is not executed at the start of the
                # loop
                return True

        return False
        