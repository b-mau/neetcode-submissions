class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # searching matching array 
        left = 0 
        right = len(matrix)
        arr = []
        while left < right:
            mid = (left + right) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                arr = matrix[mid]
                break
            elif target > matrix[mid][-1]:
                left = mid + 1
            else:
                right = mid 
        print(arr)
        
        # searching matching value in the array
        left = 0
        right = len(arr)
        while left < right:
            mid = (left + right) // 2
            if target == arr[mid]:
                return True
            elif target < arr[mid]:
                right = mid
            else:
                left = mid + 1
        return False
            
