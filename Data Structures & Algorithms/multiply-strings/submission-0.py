class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        total = 0
        n = len(num1) - 1
        m = len(num2) - 1

        for i in range(n, -1, -1):
            d1 = (ord(num1[i]) - ord("0")) * 10**(n - i)
            for j in range(m, -1, -1):
                d2 =( ord(num2[j]) - ord("0")) * 10**(m - j)
                total += d2 * d1

        return str(total)

