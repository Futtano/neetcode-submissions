class Solution:
    # Time: O(n * C_n), where C_n is the nth Catalan number
    # Space: O(n) auxiliary space, excluding the output
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(cur, opened, closed):
            if len(cur) == 2 * n:
                res.append(''.join(cur))
                return

            if opened < n:
                cur.append('(')
                backtrack(cur, opened + 1, closed)
                cur.pop()

            if closed < opened:
                cur.append(')')
                backtrack(cur, opened, closed + 1)
                cur.pop()

        backtrack([], 0, 0)
        return res