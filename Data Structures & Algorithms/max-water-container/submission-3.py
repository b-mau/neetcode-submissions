class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        maximum = (right - left) * min(heights[left], heights[right])
        area = 0
        while left < right:
            area = (right - left) * min(heights[left], heights[right])
            maximum = max(area, maximum)
            if heights[left] < heights[right]:
                left +=1
            else:
                right -=1
        return maximum

        