class Solution:
    # Time 
    # Space
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for s in strs:
            # anagrams become the same string
            srtd_s = str(sorted(s))
            if srtd_s in hashmap:
                # append the string with other anagrams
                hashmap[srtd_s].append(s)
            else:
                # add a new key to the hashmap
                hashmap[srtd_s] = [s]

        return [hashmap[key] for key in hashmap.keys()]
