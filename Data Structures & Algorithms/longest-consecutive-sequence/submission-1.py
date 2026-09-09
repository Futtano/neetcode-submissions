class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)

        longest = 0
        for el in hash_set:
            if el-1 not in hash_set:
                seq_len = 1
                while el + 1 in hash_set:
                    seq_len += 1
                    el += 1
                longest = max(longest, seq_len)

        return longest