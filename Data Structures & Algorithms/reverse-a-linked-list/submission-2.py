# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # pointer to the head of the reversed portion, initially None
        prev = None 
        
        # pointer to the item being processed
        cur = head
        
        while cur:
            # pointer to the remaining portion of the list
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        return prev 