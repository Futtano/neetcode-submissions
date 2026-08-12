class Solution:
    # Time: O((n+m)log(m+n)) sorting of two strings
    # Space O(1) space of characters and numbers 

    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)