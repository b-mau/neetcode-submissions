class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix_max_arr = [0] * n
        pref_max = 0
        for i in range(0,n):
            pref_max = max(pref_max, height[i])
            prefix_max_arr[i] = pref_max
        print(prefix_max_arr)

        
        suffix_max_arr = [0] * n
        suff_max = 0
        for i in range(n-1,-1,-1):
            suff_max = max(suff_max, height[i])
            suffix_max_arr[i] = suff_max
        print(suffix_max_arr)

        total = 0

        for i in range(0, len(height)):
            total += min(prefix_max_arr[i], suffix_max_arr[i]) - height[i]

        return total