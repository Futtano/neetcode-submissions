class Solution:
    # Naive Backtracking
    # Time: O(2^(t/m)) where m is the minimum value in nums and t is the target
    # Space: O(t/m) where m is the minimum value in nums and t is the target
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, comb, cur_sum):
            if cur_sum == target:
                res.append(comb.copy())
                return
            if i >= len(nums) or cur_sum > target:
                return

            comb.append(nums[i])
            backtrack(i, comb, cur_sum + nums[i])

            comb.pop()
            backtrack(i+1, comb, cur_sum)

        backtrack(0, [], 0)    

        return res

            