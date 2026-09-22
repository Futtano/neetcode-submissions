class Solution:
    # Time: O(n * 2^n) (additional n is for subset copy)
    # Space: O(n) for the recursion stack
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def backtrack(i):
            if i == len(nums):
                res.append(subset.copy())
                return

            # Append this item branch
            subset.append(nums[i])
            backtrack(i+1)

            # Not append this item branch
            subset.pop()
            backtrack(i+1)

        backtrack(0)

        return res
        
            
            

