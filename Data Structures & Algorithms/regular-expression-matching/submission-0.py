class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}

        def dp(i: int, j: int) -> bool:
            if (i, j) in cache:
                return cache[(i, j)]
            if j == len(p):
                return i == len(s)


            valid_char = s[i] == p[j] or p[j] == '.' if i < len(s) else False  
            result = False
            recurse_match = j+1 < len(p) and p[j+1] == '*' 
            if recurse_match:
                result = dp(i, j+2) # 0-match case 
            if valid_char and recurse_match:
                result = result or dp(i+1, j) # match 1 or more
            if valid_char and not recurse_match:
                result = dp(i+1, j+1)
            
            cache[(i, j)] = result

            return cache[(i, j)]

        return dp(0, 0)
             
            