class Solution:
    # Max heap of size k to keep track of the k closest elements
    # Let n be len(points) and k the number of items to return
    # Time complexity: O(n logk)
    # Space complexity: O(k)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Fill up the array of size k to be used as a max-heap with the initial
        # elements
        maxHeap = [ # remember to negate because we need a max-Heap and Python uses min-heaps
            (-(points[i][0]**2 + points[i][1]**2), points[i])
            for i in range(k)
        ] # O(k) time, O(k) space

        # heapify the array O(k) time
        heapq.heapify(maxHeap)

        # Process the other elements O(n - k) = O(n)
        for i in range(k, len(points)):
            point = points[i]
            x, y = point
            
            # Calculate distance and negate
            distSq = x**2 + y**2

            if distSq < -maxHeap[0][0]:
                # Replace and restore heap property
                # O(log k+1) time
                heapq.heapreplace(maxHeap, (-distSq, point))

        return [el[1] for el in maxHeap]
