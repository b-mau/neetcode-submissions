class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        count1 = {}
        for char in s1:
            if char not in count1:
                count1[char] = 1
            else:
                count1[char] += 1
        
        count2 = {}
        left, right = 0, len(s1) - 1

        for i in range(left, right + 1):
            if s2[i] not in count2:
                count2[s2[i]] = 1
            else:
                count2[s2[i]] += 1
        
        if count2 == count1:
                return True

        while right+1 <= len(s2)-1:
            count2[s2[left]] -= 1
            if count2[s2[left]] == 0:
                count2.pop(s2[left])
            left += 1
            right += 1
            if s2[right] not in count2:
                count2[s2[right]] = 1
            else:
                count2[s2[right]] += 1
            if count2 == count1:
                return True
            
        return False