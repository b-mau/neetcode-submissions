class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, path = [], []

        def backtrack(start):
            res.append(path[:])                  # every node is a subset
            for i in range(start, len(nums)):
                path.append(nums[i])             # choose
                backtrack(i + 1)                 # explore (only later elements)
                path.pop()                       # un-choose

        backtrack(0)
        return res