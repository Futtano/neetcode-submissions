class Solution:
    # Greedy
    # Time: O(n)
    # Space: O(1)
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        dgas = 0
        dtank = 0
        result = 0
        for i in range(0, len(gas)):
            dgas += gas[i] - cost[i]
            dtank += gas[i] - cost[i]
            
            # No station from result through
            # i can be a valid start.
            # Try the next station with an empty tank.
            if dtank < 0:
                result = i + 1
                dtank = 0
        
        # Total gas is insufficient to complete the circuit.
        if dgas < 0:
            return -1

        return result