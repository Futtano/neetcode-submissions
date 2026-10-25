class Solution:
    # Let n be the number of words and k be the average length of a word
    # Time: O(n*k)
    # Space: O(n)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            freq = [0] * 26
            for ch in word:
                idx = ord(ch) - ord("a")
                freq[idx] += 1
            groups[tuple(freq)].append(word)

        return list(groups.values())