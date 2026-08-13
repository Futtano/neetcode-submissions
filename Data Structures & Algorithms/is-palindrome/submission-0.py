class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while(l < r):
            isalphaLeft = s[l].isalpha()
            isalphaRight = s[r].isalpha()
            if isalphaLeft and isalphaRight:
                if s[l].lower() != s[r].lower():
                    return False
                l += 1
                r -= 1
            elif isalphaLeft and not isalphaRight: 
                r -= 1
            elif isalphaRight and not isalphaLeft:
                l += 1
            else:
                l += 1
                r -= 1

        return True
