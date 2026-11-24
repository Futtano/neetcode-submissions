class Solution:
	def countSubstrings(self, s: str) -> int:
		n = len(s)
		total = 0
		
		def expand(left: int, right: int) -> int:
			count = 0
			while left >= 0 and right < n and s[left] == s[right]:
				left -= 1
				right += 1
				count += 1
			
			return count
			

		
		for i in range(n):
			for j in range(2):
				total += expand(i, i+j)

		return total
			
