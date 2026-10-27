class Solution:
    # Stack
    # Let n = len(temperatures)
    # Time: O(n)
    # Space: O(n)
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []  # Indices of days still waiting for a warmer day.

        for i, temperature in enumerate(temperatures):
            while stack and temperature > temperatures[stack[-1]]:
                previous_day = stack.pop()
                answer[previous_day] = i - previous_day

            stack.append(i)

        return answer