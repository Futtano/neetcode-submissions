class Solution:
    # Time: O(n * 2^n)
    # Space: O(n) auxiliary, O(n * 2^n) including output
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[]]

        def backtrack(i, cur):
            if i >= len(nums):
                return

            # Include nums[i]
            cur.append(nums[i])
            res.append(cur.copy())
            backtrack(i + 1, cur)

            # Exclude nums[i] and all its duplicates
            cur.pop()

            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                i += 1

            backtrack(i + 1, cur)

        backtrack(0, [])
        return res