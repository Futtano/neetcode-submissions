class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref_prod_l = [1]
        pref_prod_r = [1]

        for i in range(1, len(nums)):
            pref_prod_l.append(nums[i-1]*pref_prod_l[i-1])

        for i in range(1, len(nums)):
            pref_prod_r.append(nums[len(nums)-i]*pref_prod_r[i-1])

        res = [ 
            pref_prod_l[i] * pref_prod_r[len(nums) - 1 - i]
            for i in range(0, len(nums))
        ]

        return(res)