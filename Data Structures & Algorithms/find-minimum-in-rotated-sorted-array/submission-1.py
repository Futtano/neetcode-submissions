class Solution:
    # Exact Match Binary Sort
    # Time: O(log(n))
    # Space: O(1)
    def findMin(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums) - 1
        res = nums[lo]

        while lo <= hi:
            if nums[lo] < nums[hi]:
                # low to hi is sorted, the minimum is nums[lo]
                res = min(res, nums[lo])
                break

            mid = lo + (hi - lo) // 2
            res = min(res, nums[mid])
            if nums[lo] <= nums[mid]:
                # low to mid is sorted, minimum must be on the other half
                lo = mid + 1
            else:
                hi = mid - 1

        return res