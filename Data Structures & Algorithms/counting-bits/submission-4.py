class Solution:
	def countBits(self, n: int) -> List[int]:
		res = [0 for i in range(n+1)]		

		for i in range(1, len(res)):
			res[i] = 1 + res[i & (i-1)]
			
		return res