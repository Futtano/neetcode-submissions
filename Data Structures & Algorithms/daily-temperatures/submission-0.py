class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0 for i in range(len(temperatures))]

        for i in range(0, len(temperatures) - 1):
            stack.append(i)
            while len(stack)>0 and temperatures[i+1] > temperatures[stack[-1]]:
                res[stack[-1]] = i+1 - stack[-1]
                stack.pop()
            
        return res