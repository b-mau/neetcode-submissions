import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones_minus = []
        for stone in stones:
            stones_minus.append(-stone)
        heapq.heapify(stones_minus)

        while len(stones_minus) > 1:
            min1 = heapq.heappop(stones_minus)
            min2 = heapq.heappop(stones_minus)
            if min1 < min2:
                heapq.heappush(stones_minus, min1 - min2)
            elif min1 > min2:
                heapq.heappush(stones_minus, min2 - min1)

        return 0 if not stones_minus else -stones_minus[0]

