class Solution:
    # Time: O(n)
    # Space: O(m) (m = number of unique characters in the string)
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l, r = 0, 0

        res = 0

        # Advance r through the array
        for r, el in enumerate(s):
            # If the character pointed by r is already
            # in the set, advance l until the previous
            # occurrence is out of the string
            while el in seen:
                seen.remove(s[l])
                l += 1
            
            # Add the new character to the valid substring
            # and update result
            seen.add(s[r])
            res = max(res, r - l + 1)

        return res
