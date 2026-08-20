
from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()  # stores indices
        l = r = 0

        while r < len(nums):
            # Remove smaller values from the back of the queue
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # Remove left index if it's out of the window boundary
            if l > q[0]:
                q.popleft()

            # Append max to output once window reaches size k
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output
