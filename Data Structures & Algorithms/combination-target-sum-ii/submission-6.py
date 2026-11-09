class Solution:
    # Find unique combinations using each input occurrence at most once
    # Let n = len(candidates).
    # Time complexity: O(n log n + n * 2^n) = O(n * 2^n)
    # Space complexity: O(n) auxiliary, excluding the output
    def combinationSum2(
        self, candidates: List[int], target: int
    ) -> List[List[int]]:
        # Group duplicates and enable pruning by the remaining target.
        candidates.sort()
        path = []
        res = []

        def dfs(i: int, remaining: int) -> None:
            # Check success first, including after taking the last candidate.
            if remaining == 0:
                res.append(path.copy())
                return

            # Stop if candidates are exhausted or all remaining values are too big.
            if i == len(candidates) or candidates[i] > remaining:
                return

            # Take this occurrence and advance so it cannot be reused.
            path.append(candidates[i])
            dfs(i + 1, remaining - candidates[i])

            # Undo the take, then skip all remaining copies of this value.
            path.pop()
            while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
                i += 1
            dfs(i + 1, remaining)

        dfs(0, target)
        return res