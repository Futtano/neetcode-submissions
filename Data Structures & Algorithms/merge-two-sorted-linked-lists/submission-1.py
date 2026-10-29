# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Let n = len(list1) and m = len(list2)
    # Time complexity: O(n + m)
    # Space complexity: O(1)
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while True:
            # Stop comparing when either list is exhausted.
            if not list1 or not list2:
                # If any of the two is fully consumed
                # merge the other one immediately
                # Handles both empty lists gracefully
                l = list1 or list2
                tail.next = l
                break

            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            # Advance tail by one as we process at least one item
            # or we merge the remaining list and break out of the
            # loop
            tail = tail.next

        return dummy.next
            

