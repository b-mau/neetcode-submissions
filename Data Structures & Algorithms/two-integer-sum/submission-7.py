class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash1 = {}
        for index,num in enumerate(nums):
            remainder = target - num
            if remainder in hash1:
                return [hash1[remainder], index]
            hash1[num] = index
            
