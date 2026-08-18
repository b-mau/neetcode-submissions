class TimeMap:

    def __init__(self):
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store.keys():
            self.store[key] = [(timestamp, value)]
        else:
            self.store[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        ls = self.store.get(key, [])
        res = ""
        left, right = 0, len(ls) - 1
        
        while left <= right:
            mid = (left + right) // 2
            (time, val) = ls[mid]
            if time <= timestamp:
                res = val
                left = mid + 1
            elif time > timestamp:
                right = mid - 1
        
        return res

