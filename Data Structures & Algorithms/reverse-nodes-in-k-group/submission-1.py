# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Recursion solution
    # Time: O(n)
    # Space: O(n/k) = O(n)

    def getKth(self, groupPrev, k):
        cur = groupPrev
        while cur and k > 0:
            cur = cur.next
            k -=1

        return cur

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Dummy ListNode before head
        dummy = ListNode(0, head)

        # Node before the start of the group
        groupPrev = dummy

        while True:
            # Get the k-th node of the group
            kth = self.getKth(groupPrev, k)
            if not kth: # if it is null, no more group to process
                break

            # The node after the end of this group
            groupNext = kth.next

            # Reverse the group
            prev, cur = kth.next, groupPrev.next
            while cur != groupNext:
                tmp = cur.next
                cur.next = prev
                prev, cur = cur, tmp

            # Save the pointer to the former head of the group
            # (now became the tail)
            tmp = groupPrev.next
            # Link the previous node before the start of the group
            # to the new head (former tail)
            groupPrev.next = kth
            # The former head (now tail) of the group becomes the node
            # before the start of the next group
            groupPrev = tmp

        return dummy.next

