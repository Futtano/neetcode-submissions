class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.k = k
        self.data = []
        for el in points:
            self.push((self.distance(*el), el))

        return [el[1] for el in self.data]

    def distance(self, x, y):
        return -(x**2 + y**2)**(1/2)

    def push(self, el):
        if len(self.data) < self.k:
            heapq.heappush(self.data, el)
        elif el[0] > self.data[0][0]:
            heapq.heapreplace(self.data, el)
