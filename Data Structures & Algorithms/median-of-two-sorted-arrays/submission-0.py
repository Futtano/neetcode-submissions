class Solution:
    # Time: O(log2(min(m, n)))
    # Space: O(1)
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_length = len(nums1) + len(nums2)
        half = total_length // 2   

        A , B = nums1, nums2 
        if len(nums1) > len(nums2): 
            A, B = B, A

        lo = 0
        hi = len(A)

        while lo <= hi:
            i = lo + (hi - lo) // 2
            j = half - i
            Aleft = A[i-1] if i > 0 else float('-inf')
            Bleft = B[j-1] if j > 0 else float('-inf')
            Aright = A[i] if i < len(A) else float('inf')
            Bright = B[j] if j < len(B) else float('inf')

            if Bleft > Aright:
                # Move cut in A to the right
                # 1 | 2      1 2 |                
                # 3 | 4    | 3 4
                lo = i + 1
            elif Aleft > Bright:
                # Move cut in A to the left
                # 4 | 5    | 4 5                
                # 2 | 3      3 4 |
                hi = i - 1
            else:
                lowerMid, higherMid = max(Aleft, Bleft), min(Aright, Bright)
                median = (lowerMid + higherMid) / 2 if total_length % 2 == 0 else higherMid
                return median 

        
