class Solution:
    # Time: O(n)
    # Space: O(n)
    def findDuplicate(self, nums: List[int]) -> int:  
    # Intuition: treat the array as a linked list where
    # the next pointer, for each index i, is nums[i].
    # To detect the duplicate, mark each visited node with
    # -1. Follow the list. If the current node brings us to
    # -1, that's a duplicate

        curr = 0
        nxt = nums[curr]

        while nxt != -1:
            nums[curr] = -1
            curr = nxt
            nxt = nums[nxt]

        return curr
            
        