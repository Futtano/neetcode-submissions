class Solution:
    # Stack
    # Let n = len(temperatures)
    # Time: O(n)
    # Space: O(n)
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        out = [0] * len(temperatures)

        for i in range(n - 1, -1, -1):
            while stack:
                j = stack[-1]
                tmp = temperatures[j]
                if tmp > temperatures[i]:
                    out[i] = j - i
                    break
                stack.pop()
            stack.append(i)

        return out
