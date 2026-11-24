class Solution:
	def longestPalindrome(self, s: str) -> str:
		n = len(s)
		dp = [[False for _ in range(n)] for _ in range(n)]
		best = 1
		res = (0, 1)
		
		for i in range(n):
			dp[i][i] = True
		
		for i in range(1, n):
			dp[i-1][i] = s[i-1] == s[i]
			if dp[i-1][i]:
				res = (i-1,i+1)


		for l in range(n-2, -1, -1):
			for r in range(l+2, n):
				dp[l][r] = s[l] == s[r] and dp[l+1][r-1]
				if dp[l][r] and r - l + 1 > best:
					best = r - l + 1
					res = (l, r+1)

		start, end = res
		return s[start: end]