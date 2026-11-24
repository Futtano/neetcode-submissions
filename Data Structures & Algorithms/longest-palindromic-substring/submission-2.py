class Solution:
	def longestPalindrome(self, s: str) -> str:
		n = len(s)
		start, end = 0, 1
		

		def expand(left: int, right: int) -> tuple[int, int]:
			while left >= 0 and right < n and s[left] == s[right]:
				left -= 1
				right += 1

			return left+1, right

		
		for i in range(n):
			for j in range(2):
				l, r = expand(i, i+j)
				if r - l > end - start:
					start, end = l, r

		return s[start :end]