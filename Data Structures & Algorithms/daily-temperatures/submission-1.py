class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for ind,temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                stack_index, stack_temp = stack.pop()
                result[stack_index] = ind - stack_index
            stack.append((ind, temp))
        return result