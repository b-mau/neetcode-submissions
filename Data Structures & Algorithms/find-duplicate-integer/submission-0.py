class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        # Phase 2: find the entrance to the cycle (== the duplicate).
        # One pointer restarts at the true head (index 0, NOT nums[0]).
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow