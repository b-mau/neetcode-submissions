class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for index in range(0,len(nums)):
            if index > 0 and nums[index] == nums[index - 1]:
                continue

            target = -nums[index]
            left = index + 1
            right = len(nums) - 1

            while left < right:
                current_sum = nums[left] + nums[right]
                
                if current_sum == target:
                    result.append([nums[index], nums[left], nums[right]])
                    left += 1
                    
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                        
                elif current_sum < target: 
                    left += 1
                else:
                    right -= 1

        return result