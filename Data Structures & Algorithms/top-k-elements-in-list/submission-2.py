class Solution:
    # Bucket sort
    # Time: O(n)
    # Space: O(n) 
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # An array of buckets indexed by frequency
        freq_buck = [[] for _ in range(len(nums) + 1)]

        # Count occurrence of each num
        value_counts = {}
        for v in nums:
            value_counts[v] = 1 + value_counts.get(v, 0)
        
        # Insert each num in the corresponding frequency bucket
        for v, c in value_counts.items():
            freq_buck[c].append(v)

        # Iterate over the frequency bucket array in reverse order
        # (from most to least frequent)
        result = []
        for i in range(len(nums), 0, -1):
            for num in freq_buck[i]:
                # Append numbers into the bucket to result
                result.append(num)
                # If we reached k elements, we can return
                if len(result) == k:
                    return result
