class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [1] * n
        current = 1
        for i in range(0,n):
            pref[i] = current
            current = current * nums[i]
        
        suf = [1] * n
        current = 1
        for i in range(n-1,-1,-1):
            suf[i] = current
            current = current * nums[i]
        
        
        final = [1] * n
        for i in range(0,n):
            final[i] = pref[i] * suf[i]
        
        return final

