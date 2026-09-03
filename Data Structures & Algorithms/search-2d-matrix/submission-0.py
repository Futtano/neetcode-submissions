class Solution:
    # Time: O(log(n*m))
    # Space: O(1)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        
        lo = 0
        hi =  (rows * cols) - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            row_idx = mid // cols
            col_idx = mid % cols
            
            if matrix[row_idx][col_idx] == target:
                return True
            elif matrix[row_idx][col_idx] < target:
                lo = mid + 1
            else:
                hi = mid - 1

        return False