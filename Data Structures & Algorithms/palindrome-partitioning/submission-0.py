class Solution:
    # Time: O(n * 2^n) (number of places where we can make the cut)
    # Space: O(n) to store partial results (path)
    def partition(self, s: str) -> List[List[str]]:
        result = []
        path = []

        def isPalindrome(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            
            return True

        def backtrack(start):
            # We used the entire string
            if start == len(s):
                result.append(path.copy())
                return

            # Try every possible substring s[start: end+1]
            for end in range(start, len(s)):
                if isPalindrome(start, end):
                    path.append(s[start:end+1])
                    backtrack(end+1)

                    # Undo the choice
                    path.pop()

        backtrack(0)

        return result
    