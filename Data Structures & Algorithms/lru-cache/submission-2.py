class LRUCache:

    # use a stack to track the least recently used one
    # use a dictionary to keep track of each one
    def __init__(self, capacity: int):
        self.values = {}
        self.lru = []
        self.current_cap = 0
        self.max_capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.values.keys():
            return -1
        else:
            val = self.values[key]
            self.lru.remove((key, val))
            self.lru.append((key,val))
            return self.values[key]

    def put(self, key: int, value: int) -> None:
        if key in self.values.keys():
            val = self.values[key]
            self.lru.remove((key, val))
            self.values[key] = value
            self.lru.append((key,value))
        else:
            if self.current_cap == self.max_capacity:
                old_key, old_val = self.lru[0]
                self.lru = self.lru[1:]
                self.values.pop(old_key)
            else:
                self.current_cap += 1
            self.lru.append((key,value))
            self.values[key] = value
