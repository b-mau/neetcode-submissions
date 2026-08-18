import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left <= right:
            mid = (left + right) // 2
            counter = 0
            for val in piles:
                counter += math.ceil(val/mid)
            
            if counter > h:
                left = mid + 1
            if counter <= h:
                right = mid - 1
        
        return left


# must perform binary search to find the smallest time. but what do you search over?
# try the value of h from the smallest value. 
# not right, as seen by the 25 second example.
# therefore, perform binary search over the maximum value in the array. 
# there is O(n) complexity, so you are expected to take out the maximum one
# now you need to check how many bananas are eaten with that rate. that's just iterating over the array, and finding the 
