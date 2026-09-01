class Solution:
    # Time:     O(n)
    # Space:    O(m) (where m = number of unique characters)

    # This is the standard solution which involves scanning the whole hashmap
    # to find the most frequent character in the substring. It takes O(26n) which
    # is still technically linear time
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        l = res = 0

        for r in range(len(s)):
            # Update the count for the current character pointed
            # by r in the substring
            counts[s[r]] = counts.get(s[r], 0) + 1
            
            # Update biggest frequency
            most_freq = 0
            for count in counts.values():
                most_freq = max(most_freq, count)
            
            # Check if the substring is valid and if it isn't,
            # advance l until it is again valid
            while (r - l + 1) - most_freq > k:
                # Update count of items in the substring
                counts[s[l]] -= 1
                l += 1
            # Update result
            res = max(r - l + 1, res)

        return res 