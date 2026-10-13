class Solution:
    # Optimal solution
    # Time: O(n)
    # Space O(1)
    def countBits(self, n: int) -> List[int]:
        cache = [0] * (n + 1)
        
        for i in range(1, n+1):
            cache[i] = cache[i >> 1] + (i & 1)

        return cache