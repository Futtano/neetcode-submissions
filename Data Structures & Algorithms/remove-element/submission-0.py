class Solution:
    # In-place compaction, read-write pointers
    # Time complexity: O(n)
    # Space complexity: O(1)
    def removeElement(self, nums: List[int], val: int) -> int:
        removed = 0
        n = len(nums)

        for i in range(n):
            if nums[i] == val:
                # Count the number of items equal
                # to val to the left of the next valid item
                removed += 1
            else:
                # Move the valid item to its correct position
                nums[i - removed] = nums[i]

        return n - removed