class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        longest = 0
        for n in hash_set:
            if n-1 not in hash_set:
                # Begin counting seq
                cur = 1
                while n+1 in hash_set:
                    cur += 1
                    n +=1
                longest = max(cur, longest)


        return longest
        