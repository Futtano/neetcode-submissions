class Solution:
    # Time: O(nlogn)
    # Space: O(n) 
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count frequencies with an hash map
        freq = {}
        for el in nums:
            freq[el] = 1 +freq.get(el, 0)
        
        # Sort el by frequency
        top_freq = sorted(
            (k for k in freq.keys()),
            key = lambda k: freq[k],
            reverse=True,
        )

        return top_freq[:k]