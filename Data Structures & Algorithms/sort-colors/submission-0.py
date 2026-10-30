class Solution:
    # Counting sort over a fixed value range
    # Two iteration version
    # Time complexity: O(n)
    # Space complexity: O(1)
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0] * 3 # to track item counts

        # count items
        for el in nums:
            counts[el] +=1 
        
        # overwrite the nums array, starting
        # from the lower indexes of count
        i = j = 0
        while i < len(nums) and j < len(counts):
            if counts[j] > 0:
                # still items with index j to add 
                nums[i] = j
                counts[j] -= 1 
                i += 1
            else:
                # move to the next j
                j += 1
