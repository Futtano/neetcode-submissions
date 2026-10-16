class Solution:
    # Greedy
    # Time: O(n)
    # Space: O(1)
    def checkValidString(self, s: str) -> bool:
        open_low_bound = open_high_bound = 0
        for ch in s:
            if ch == '(':
                open_low_bound += 1
                open_high_bound += 1
            elif ch == ')':
                open_low_bound -= 1
                open_high_bound -= 1
            else:
                open_low_bound -= 1
                open_high_bound += 1

            if open_high_bound < 0:
                return False
            open_low_bound = max(0, open_low_bound)
        
        return open_low_bound == 0