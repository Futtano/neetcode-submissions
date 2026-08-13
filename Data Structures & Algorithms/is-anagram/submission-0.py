class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # For effieciency, if s and t are not the same length
        # they cannot be anagrams
        if len(s) != len(t):
            return False

        # An anagram must have the same exact count of letters
        freq = {}
        for ch in s: # Build the frequency count for each letter of s
            freq[ch] = freq.setdefault(ch, 0) + 1

        for ch in t: # check if s has the same exact frequency of characters
            if freq.get(ch) is None or freq[ch] == -1: # if the letter is not in s or t has more letters of this kind than s
                return False
            freq[ch] -= 1 # decrease the number of available letters of this kind

        return True