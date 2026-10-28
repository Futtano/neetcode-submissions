class Solution:
    # Two pointers and set
    # Time complexity: O(n)
    # Space complexity: O(min(n, A)), where A is the alphabet size.
    # O(1) under the fixed printable-ASCII constraint.
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = r = 0

        res = 0

        while r < len(s):
            # Advance r until a duplicate is found
            while r < len(s) and s[r] not in seen:
                seen.add(s[r])
                r += 1

            # Update res
            res = max(res, r - l)

            # Remove characters from the left until the incoming s[r]
            # no longer has an earlier occurrence in the window.
            while r < len(s) and s[r] in seen:
                seen.remove(s[l])
                l += 1

        return res
            