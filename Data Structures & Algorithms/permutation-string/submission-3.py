class Solution:
    # Time: O(n)
    # Space: O(m) where m is the length of s1
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l , r = 0, len(s1) - 1

        # Construct hashmap for s1 and s2[0, len(s1)]
        hm1 = {}
        hm2 = {}
        for c1, c2 in zip(s1, s2[0:len(s1)]):
            hm1[c1] = 1 + hm1.get(c1, 0)
            hm2[c2] = 1 + hm2.get(c2, 0)
        
        print(hm1)
        print(hm2)

        while r < len(s2):
            # If hashmap match, the substring is a valid permutation
            # and we can return
            if hm1 == hm2:
                return True
            
            # Remove the occurrences of the LEFT end of
            # s2 (i.e s2[l])
            hm2[s2[l]] -= 1
            if not hm2[s2[l]]:
                del hm2[s2[l]]
            # Move window forward by one step
            l += 1
            r += 1
            # Update occurrences with the new character 
            # inside the window (i.e s[r]), if we have 
            # not reached the end of the string
            if r < len(s2):
                hm2[s2[r]] = 1 + hm2.get(s2[r], 0)

        return False