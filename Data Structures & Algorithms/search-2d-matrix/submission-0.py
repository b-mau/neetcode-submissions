class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Finding the row
        left = 0 
        right = len(matrix) - 1

        m = float('inf')

        while left <= right:
            mid = (left + right) // 2
            if matrix[mid][0] <= target <= matrix[mid][len(matrix[0])-1]:
                m = mid
                break
            elif target < matrix[mid][0]:
                right = mid - 1
            elif target > matrix[mid][len(matrix[0])-1]:
                left = mid + 1

        if m != float('inf'):
            pass
        else:
            return False
        
        # Finding if the value is inside the range
        left = 0 
        right = len(matrix[m])
        while left <= right:
            mid = (left + right) // 2
            if matrix[m][mid] == target:
                return True
            elif matrix[m][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False



        