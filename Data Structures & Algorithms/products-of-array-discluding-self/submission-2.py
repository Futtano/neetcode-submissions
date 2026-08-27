class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_prods, r_prods = [1], [1]
        l_prods.extend((l_prods[i-1] * nums[i-1] for i in range(1, len(nums))))
        r_prods.extend((r_prods[i-1] * nums[len(nums)-i] for i in range(1, len(nums))))

        return [l_prods[i] * r_prods[len(nums)-1-i] for i in range(0, len(nums))]