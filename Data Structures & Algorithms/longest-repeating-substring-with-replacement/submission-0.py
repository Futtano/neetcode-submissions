class Solution:
    # Time:     O(n)
    # Space:    O(m) (where m = number of unique characters)
    def characterReplacement(self, s: str, k: int) -> int:
        char_freq = {}
        l = r = res = 0
        max_freq = 0

        while r < len(s):
            char_freq[s[r]] = char_freq.get(s[r], 0) + 1
            max_freq = max(max_freq, char_freq[s[r]])
            
            while (r - l + 1) - max_freq > k:
                char_freq[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
    
        return res

            