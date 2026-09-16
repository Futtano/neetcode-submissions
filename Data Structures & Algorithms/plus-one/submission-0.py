class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        result = [0] * (len(digits) + 1)
        
        for i in range(len(result)-1, 0, -1):
            tot = digits[i-1] + carry
            result[i] = tot % 10
            carry =  tot // 10
        
        if carry == 1:
            result[0] = 1
            result[1] = 0
            return result
        return result[1:]
