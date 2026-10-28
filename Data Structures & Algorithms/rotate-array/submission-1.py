class Solution:
    # Cycle Replacement
    # Time complexity: O(n)
    # Space complexity: O(1)
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        if k % n == 0:
            # This rotation would not change any position
            return

        moves = 0
        start = i = 0
        to_move = nums[start]

        while moves < n:
            j = (i + k) % n
            displaced = nums[j]
            nums[j] = to_move
            to_move = displaced
            moves += 1
            i = j
            if i == start and moves < n:
                # to continue looping if moves < n
                start += 1
                i = start
                to_move = nums[start]