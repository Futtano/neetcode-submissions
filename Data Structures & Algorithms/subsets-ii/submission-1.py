class Solution:
    # Time: O(n * 2^n)
    # Space: O(n) auxiliary, O(n * 2^n) including output
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(start, cur):
            res.append(cur.copy())

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue

                cur.append(nums[i])
                backtrack(i + 1, cur)
                cur.pop()

        backtrack(0, [])
        return res