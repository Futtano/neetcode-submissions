class Solution:
    # Greedy
    # Time: O(n)
    # Space: O(1)
    def jump(self, nums: List[int]) -> int:
        moves = 0 # Number of moves
        current_end = 0  # Furthest index reachable with `moves` jumps
        farthest = 0     # Furthest index reachable with one additional jump

        for i in range(len(nums) - 1):  # Exclude the destination: no jump needed from it
            farthest = max(farthest, i + nums[i])
            if i == current_end:  # Finished scanning the current jump's range
                moves += 1
                current_end = farthest
               

        return moves