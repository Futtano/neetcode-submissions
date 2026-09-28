class Solution:
    # Time: O(L * 4^L) (also account for string copy)
    # Space: O(L)
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []
        def backtrack(i, seq):
            if i == len(digits):
                res.append("".join(seq))
                return

            for ch in mapping[digits[i]]:
                seq.append(ch)
                backtrack(i+1, seq)
                seq.pop()

        backtrack(0, [])
        return res