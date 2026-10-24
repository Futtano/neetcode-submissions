class Solution:
    # Time: O(nlogn)
    # Space: O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_idxs = sorted(
            range(len(nums)),
            key=lambda i: nums[i]
        )

        l, r = 0, len(nums) - 1

        while l < r:
            i, j = sorted_idxs[l], sorted_idxs[r]
            total = nums[i] + nums[j]
            if total < target:
                l += 1
            elif total > target:
                r -= 1
            else:
                break

        low = sorted_idxs[l]
        high = sorted_idxs[r]
        if  low > high:
            low, high = high, low
        return [low, high]