class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        seen.add(n)
        while n != 1:
            partial = 0
            while n > 0:
                partial += (n % 10)**2
                n = n // 10
            n = partial
            if n in seen:
                return False
            seen.add(n)

        return True
