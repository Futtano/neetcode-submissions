class Solution:
    # Leftmost boundary binary search template
    # Time: O(n*log(k)) where k is the max number in piles
    # Space: O(1)
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = 1 # the minimum possible rate is one banana per hour
        # The max rate we search for is the one that allows to clear
        # each pile in one hour, i.e the max number in piles
        hi = max(piles)  

        while lo < hi:
            mid = lo + (hi - lo) // 2
            # Calculate the time it takes to eat all the bananas with this rate
            tot_time = sum(math.ceil(pile/mid) for pile in piles) 
            if tot_time > h: # if we take more than h, the solution is towards a higher rate
                lo = mid + 1
            else: # if we take less or equal than h, the solution is towards lower rates
                hi = mid
        
        return lo
