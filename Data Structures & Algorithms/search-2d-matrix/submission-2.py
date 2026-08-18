class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # searching matching array 
        left = 0 
        right = len(matrix) - 1
        arr = []
        while left <= right:
            mid = (left + right) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                arr = matrix[mid]
                break
            elif target > matrix[mid][-1]:
                left = mid + 1
            else:
                right = mid -1
        print(arr)
        
        # searching matching value in the array
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if target == arr[mid]:
                return True
            elif target < arr[mid]:
                right = mid -1
            else:
                left = mid + 1
        return False
            
