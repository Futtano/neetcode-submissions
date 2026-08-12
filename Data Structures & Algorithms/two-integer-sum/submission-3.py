class Solution: 
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # A simple hashmap to track which numbers 
        # we already seen and their indexes
        seen = {}

        for i, n in enumerate(nums):
            # to match target, we need to add this
            toAdd = target - n
            if toAdd in seen: # if we already seen this value
                return [seen[toAdd], i] # return the indexes in this order
            
            # Add the current number to the hashmap
            seen[n] = i

        # Dead code, solution always exist
        return 0, 0