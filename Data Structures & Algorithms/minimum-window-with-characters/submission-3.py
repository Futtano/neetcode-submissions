class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        freq_t = {}
        freq_sub = {}
        res = None

        # Fill up freq_t
        for ch in t:
            freq_t[ch] = 1 + freq_t.get(ch, 0)

        l = 0
        r = 0

        # Number of equal characters to be in the window and current formed count
        # (NOTE: to update formed, the count of characters should also match)
        required = len(freq_t)
        formed = 0

        while r < len(s):
            # Search for the minimum valid substring
            # starting at l by increasing r
            while r < len(s) and formed < required:
                freq_sub[s[r]] = 1 + freq_sub.get(s[r], 0)
                if s[r] in freq_t and freq_sub[s[r]] == freq_t[s[r]]:
                    formed += 1
                r += 1

            # Try stretching the string by increasing l
            # until we invalidate the invariant again
            while formed == required:
                # The substring is valid, update res
                res = (l, r) if res is None or (r-l) < (res[1] - res[0]) else res

                freq_sub[s[l]] -= 1
                if s[l] in freq_t and freq_sub[s[l]] == freq_t[s[l]] - 1:
                    formed -= 1
                l += 1


        return "" if res is None else s[res[0]: res[1]] 

