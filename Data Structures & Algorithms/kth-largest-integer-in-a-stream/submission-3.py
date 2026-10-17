import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        heapq.heapify(self.heap)
        self.k = k
        while len(self.heap) > k:
            heapq.heappop(self.heap)


    def add(self, val: int) -> int:
        heap = self.heap
        if len(heap) < self.k:
            heapq.heappush(heap, val)
        else:
            if val > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, val)
        
        return heap[0]
