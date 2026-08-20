# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Suboptimal with recursion
    # Time: O(N)
    # Space: O(N) (stack frame)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Early return if list is empty
        if not head:
            return head

        # Set this node as the new head
        newHead = head

        # If this is not the end node
        if head.next:
            # get the new head from the recursive call
            newHead = self.reverseList(head.next)
            
            # reverse the next pointer to the current node
            head.next.next = head
        
        # IMPORTANT: to avoid cycles, the last node should point to None
        head.next = None

        return newHead

