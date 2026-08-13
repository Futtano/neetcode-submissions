class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort the list of str
        srtd_strs = sorted(strs)

        # Transform each entry in a hashmap of letter frequencies
        freq_list = []
        for s in srtd_strs:
            freq = {}
            for ch in s:
                freq[ch] = freq.setdefault(ch, 0) + 1
            freq_list.append(freq)

        # two pointers to merge the same freq map into a common list
        slow = 0
        result = []
        for fast in range(1, len(freq_list)):
            if freq_list[slow] != freq_list[fast]:
                result.append(list(srtd_strs[slow:fast]))
                slow = fast
        
        result.append(list(srtd_strs[slow:]))
        return result

        