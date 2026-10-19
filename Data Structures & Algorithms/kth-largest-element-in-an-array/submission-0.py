import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        result = []
        for num in nums:
            if len(result) < k:
                heapq.heappush(result, num)
            else:
                if result[0] < num:
                    heapq.heappop(result)
                    heapq.heappush(result, num)
        return result[0]