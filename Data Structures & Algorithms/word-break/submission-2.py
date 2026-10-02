class Solution:
    # Time: O(n * Sum(len(word) for word in words))
    # Space: O(n)
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = [None for _ in range(len(s))]

        def canBreak(start: int) -> bool:
            if start == len(s):
                return True
            if cache[start] is not None:
                return cache[start]

            for word in wordDict:
                if (
                    s.startswith(word, start) and
                    canBreak(start + len(word))
                ):
                    cache[start] = True
                    return True

            cache[start] = False
            return False
        
        return canBreak(0)