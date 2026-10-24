class Solution:
    # Prefix Prod optimal
    # Time: O(n)
    # Space: O(1)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Build right->left prefix product
        res = [1] * len(nums)
        for i in range(len(nums)-2, -1, -1):
            # res[i] is the product of items right of i
            res[i] = res[i+1] * nums[i+1]

        # cur keeps track of left-> right prod
        cur = 1
        for i in range(len(res)):
            res[i] = cur * res[i]
            cur *= nums[i]

        return res