class Solution:
    # Binary search in a rotated sorted array with distinct values
    # Let n = len(nums).
    # Time complexity: O(log n)
    # Space complexity: O(1)
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        # If the target exists, it remains within [left, right].
        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            # At least one half is sorted. Equality includes a one-element half.
            if nums[left] <= nums[mid]:
                # Keep the sorted left half if its value range contains target.
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # The right half is sorted. Its range excludes the checked midpoint.
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1
