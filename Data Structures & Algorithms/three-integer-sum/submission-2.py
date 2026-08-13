class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        srtd_nums = sorted(nums)
        i = 0
        stop = len(srtd_nums) - 2
        while i < stop:
            l = i + 1
            r = len(srtd_nums) -1
            while l < r:
                total = srtd_nums[i] + srtd_nums[l] + srtd_nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    res.append(
                        [srtd_nums[i], srtd_nums[l], srtd_nums[r]]
                    )
                    r -=1
                    while(l < r and  srtd_nums[r] == srtd_nums[r+1]):
                        r -= 1

            i += 1
            while(i < stop and srtd_nums[i] == srtd_nums[i-1]):
                i += 1

        return res


    