class Solution:
    # # Two pointers with at most one branching step
    # Time: O(n)
    # Space: O(1) (At most 2 subproblems after the firs call to isPalindrome)
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(l: int, r: int, canDelete: bool) -> bool:
            while l < r and s[l] == s[r]:
                l += 1
                r -= 1

            palindrome = l >= r
            if palindrome:
                return palindrome
            if canDelete: 
                palindrome = (
                    isPalindrome(l+1, r, False) or 
                    isPalindrome(l, r-1, False)
                )
            return palindrome

        return isPalindrome(0, len(s)-1, True)
