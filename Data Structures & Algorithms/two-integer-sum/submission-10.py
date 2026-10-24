class Solution:
    # Hashmap optimal solution
    # Time: O(n)
    # Space: O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for i, el in enumerate(nums):
            # Check if we already seen it
            # before inserting
            to_match = target - el
            if to_match in hash_map:
                return [hash_map[to_match], i] # hash_map[to_match] comes first
            hash_map[el] = i

        # Will never be executed, solution is guaranteed
        return [-1, -1] 
