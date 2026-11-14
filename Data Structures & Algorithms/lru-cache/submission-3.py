class Node:
    def __init__(self, key=0, val=0):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.head, self.tail = Node(), Node()
        self.head.next, self.tail.prev = self.tail, self.head
        
    def remove(self, n):
        n.prev.next, n.next.prev = n.next, n.prev
    
    def add_front(self, n):
        n.next, n.prev = self.head.next, self.head
        self.head.next.prev = n
        self.head.next = n
    
    def get(self, key: int) -> int:
        n = self.map.get(key)
        if not n:
            return -1
        self.remove(n)
        self.add_front(n)
        return n.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            n = self.map[key]
            n.val = value
            self.remove(n)
            self.add_front(n)
            return 
        if len(self.map) == self.capacity:
            lru = self.tail.prev
            self.remove(lru)
            del self.map[lru.key]
        n = Node(key, value)
        self.map[key] = n
        self.add_front(n)
        
