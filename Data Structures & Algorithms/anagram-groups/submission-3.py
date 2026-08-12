class Solution:
    # Time: O(n*mlogm) where n is len(strs) and m is average length of each string
    # Space: O(m*n) 
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for s in strs:
            signature = [0] * 26
            # use tuple of frequencies as hashmap key
            for c in s:
                signature[ord(c) - ord('a')] += 1
            # the value will be the list that groups anagrams
            hashmap[tuple(signature)].append(s)

        return list(hashmap.values())
            
