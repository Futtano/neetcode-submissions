class Solution:
    # Time:     O(n)
    # Space:    O(m) (where m = number of unique characters)

    # This is a more clever solution which avoids scanning the hashmap every
    # time to find the character with the highest frequency in the current
    # substring. It is O(n) time instead O(26n).
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        most_freq = 0
        l = res = 0

        for r in range(len(s)):
            # Update the count for the current character pointed
            # by r in the substring
            counts[s[r]] = counts.get(s[r], 0) + 1
            
            # Update biggest frequency
            most_freq = max(most_freq, counts[s[r]])
            
            # Check if the substring is valid and if it isn't,
            # advance l until it is again valid
            while (r - l + 1) - most_freq > k:
                # Update count of items in the substring
                counts[s[l]] -= 1
                l += 1
            # Update result
            res = max(r - l + 1, res)

        return res 