class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        
        ls = sorted(count, key=lambda k: count[k], reverse = True)

        return ls[:k]
        