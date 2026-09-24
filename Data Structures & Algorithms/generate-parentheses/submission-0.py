class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(cur, opened, toClose):
            if len(cur) == 2 * n:
                res.append(''.join(cur))
                return
            
            if opened < n:
                cur.append('(')
                backtrack(cur, opened + 1, toClose+1)
                cur.pop()
            
            if toClose > 0:
                cur.append(')')
                backtrack(cur, opened, toClose-1)
                cur.pop()


        backtrack([], 0, 0)
        return res
            
            

                         
