class Solution:
    # Leftmost boundary binary search template
    # Time: O(n*log(k)) where k is the max number in piles
    # Space: O(1)
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = 1
        hi = max(piles)

        while lo < hi:
            mid = lo + (hi - lo) // 2
            tot_time = sum(math.ceil(pile/mid) for pile in piles)
            if tot_time > h:
                lo = mid + 1
            else:
                hi = mid
        
        return lo
