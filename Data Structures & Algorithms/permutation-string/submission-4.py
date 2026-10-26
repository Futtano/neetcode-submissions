class Solution:
    # Fixed sliding window with frequency counts
    # Let n = len(s1) + len(s2)
    # Time: O(n)
    # Space: O(26) = O(1)
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # s2 cannot include any possible
        # permutation of a longer string
        if len(s1) > len(s2):
            return False

        # Build frequency maps of s1 and the
        # first n1 characters of s2 where n1
        # is the length of s1
        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        # We check how many frequency counts over the 26
        # letter map match
        matches = sum(s1Count[i] == s2Count[i] for i in range(26))

        # Advance both l and r one step at a time (fixed window)
        l = 0
        for r in range(len(s1), len(s2)):
            # If we match frequencies for all the letters
            # s2 must contain a permutation of s1
            if matches == 26:
                return True

            # If adding 1 to the frequency of the new character
            # pointed by r makes a frequency match, add 1 to matches
            # otherwise ONLY if adding this one eliminates a match we
            # decrease matches
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            # If removing 1 to the frequency of the old character
            # pointed by l makes a frequency match, add 1 to matches
            # otherwise ONLY if removing this one eliminates a 
            # match we decrease matches
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            # advance l by one
            l += 1
        return matches == 26