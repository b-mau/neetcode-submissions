class Solution:
    def combinationSum(self, nums, target):
        nums.sort()              # lets us stop early (pruning)
        result = []
        path = []

        def backtrack(start, remaining):
            if remaining == 0:                 # base case: found a valid combo
                result.append(path[:])         # copy! path keeps changing
                return

            for i in range(start, len(nums)):
                if nums[i] > remaining:        # too big, and so is everything after it
                    break
                path.append(nums[i])           # 1. choose
                backtrack(i, remaining - nums[i])  # 2. explore (i, not i+1: reuse allowed)
                path.pop()                     # 3. un-choose

        backtrack(0, target)
        return result