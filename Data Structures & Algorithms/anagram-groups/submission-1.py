class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Transform each entry in a hashmap of letter frequencies
        freq_list = []
        for s in strs:
            freq = {}
            for ch in s:
                freq[ch] = freq.setdefault(ch, 0) + 1
            freq_list.append(freq)
        
        # Construct a tuple string, freq
        srtd_strs = [
            (s, tuple(sorted(freq.items())))
            for s, freq in zip(strs, freq_list)
        ]
        # Sort by the second element (frequency tuple)
        srtd_strs.sort(key=lambda x: x[1])

        # two pointers to merge the same freq map into a common list
        slow = 0
        result = []
        for fast in range(1, len(srtd_strs)):
            if srtd_strs[slow][1] != srtd_strs[fast][1]:
                result.append([s for s, _ in srtd_strs[slow:fast]])
                slow = fast
        
        result.append([s for s, _ in srtd_strs[slow:]])
        return result

        