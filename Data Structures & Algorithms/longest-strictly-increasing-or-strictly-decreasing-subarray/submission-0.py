class Solution:
    # Two pointers technique
    # Let n = len(nums)
    # Time complexity: O(n)
    # Space complexity: O(1)
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        start = 0
        end = start + 1
        best = 1

        while end < n:
            if nums[start] < nums[end]:
                while end < n and nums[end-1] < nums[end]:
                    end += 1
            elif nums[start] > nums[end]:
                while end < n and nums[end-1] > nums[end]:
                    end += 1
            else:
                start += 1
                end += 1

            best = max(best, end - start)
            start = end - 1

        return best