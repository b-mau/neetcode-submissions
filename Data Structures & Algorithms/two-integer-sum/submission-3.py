class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            difference = target - nums[i]
            new_list = nums.copy()
            new_list.remove(nums[i])
            if difference in nums[i + 1:]:
                j = nums[i + 1:].index(difference) + (i + 1)
                return [i, j]
                


        