class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search over the eating speed
        left = 1
        right = max(piles)


        while left < right:
            mid = (right + left) // 2
            time = self.eatingSpeed(piles, mid)

            # if we have exceeded the time, we need a higher value, so we increase left
            if time > h:
                left = mid + 1
            # if we still have time, we can reduce it
            else:
                right = mid
        
        # we return the smallest possible value
        return left
    
    def eatingSpeed(self, pile: List[int], k: int) -> int:
        result = 0 
        for banana in pile:
            result += math.ceil(banana / k)
        
        return result
