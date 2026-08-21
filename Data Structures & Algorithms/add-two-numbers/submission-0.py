# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        mock_head = ListNode()
        curr = mock_head
        carry = 0

        while l1 or l2:
            # Both numbers exist
            if l1 and l2:
                tot = l1.val + l2.val + carry
                carry, remainder = divmod(tot, 10)
                curr.next = ListNode(remainder)
                curr = curr.next
                l1 = l1.next
                l2 = l2.next
            elif node := l1 or l2:
                if l1:
                    l1 = l1.next
                else:
                    l2 = l2.next
                tot = node.val + carry
                carry, remainder = divmod(tot, 10)
                curr.next = ListNode(remainder)
                curr = curr.next

        if carry:
            curr.next = ListNode(carry)
            curr = curr.next
        curr.next = None
        return mock_head.next
