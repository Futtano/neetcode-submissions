class TimeMap:

    def __init__(self):
        self.storage = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.storage[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.storage[key]
        return self.bsearch(values, timestamp)

    @staticmethod
    def bsearch(values, target):
        if len(values) == 0:
            return ''

        lo = 0
        hi = len(values)

        while lo < hi:
            mid = lo + (hi - lo) // 2
            if values[mid][0] > target:
                hi = mid
            else:
                lo = mid + 1
        
        if lo == 0:
            return ''

        res = lo - 1
        return values[res][1]
        

        
