class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        totalCosts = [-1] * len(cost)
        
        def climb(step):
            if step >= len(cost):
                return 0

            if totalCosts[step] != -1:
                return totalCosts[step]
            
            totalCosts[step] = \
                cost[step] + min(climb(step+1), climb(step+2))
            return totalCosts[step]

        return min(climb(0), climb(1))