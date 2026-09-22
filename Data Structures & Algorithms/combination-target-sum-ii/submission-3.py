class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return

            cur.append(candidates[i])
            backtrack(i+1, cur, total + candidates[i])

            cur.pop()
            for j in range(i+1, len(candidates)):
                if candidates[j] != candidates[i]:
                    backtrack(j, cur, total)
                    break 

        backtrack(0, [], 0)
        return res