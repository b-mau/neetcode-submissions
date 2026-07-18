class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setnums = set()
        for num in nums:
            if num not in setnums:
                setnums.add(num)
            else:
                return True

        return False 

        