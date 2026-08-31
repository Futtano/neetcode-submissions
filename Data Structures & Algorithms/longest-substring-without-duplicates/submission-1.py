class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l, r = 0, 0
        max_len = 0

        while r < len(s):
            if s[r] in seen:
                max_len = max(max_len, r - l)
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
            
            seen.add(s[r])
            r += 1

        max_len = max(max_len, r - l)
        return max_len
