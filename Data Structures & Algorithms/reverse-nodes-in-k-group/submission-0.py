# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head, end):
        prev, cur = None, head
        
        while prev != end:
            nxt = cur.next
            cur.next = prev
            prev, cur = cur, nxt

        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        cur = head
        for i in range(k-1):
            cur = cur.next if cur else None
            if not cur: return head
        
        next_head = self.reverseKGroup(cur.next, k) # null
        newHead = self.reverse(head, cur) # 6
        head.next = next_head
        return newHead