class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
            
        sorted_keys = sorted(count.keys(), key=lambda x: count[x], reverse=True)
        return sorted_keys[:k]