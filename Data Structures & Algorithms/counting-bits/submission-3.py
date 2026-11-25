class Solution:
	def countBits(self, n: int) -> List[int]:
		res = [0 for i in range(n+1)]
		powOf2 = 1	

		for i in range(1, len(res)):
			if i == 2 * powOf2:
				powOf2 = i
			res[i] = 1 + res[i - powOf2]
			
		return res