class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0 
        maxFreq = 0 
        ans = 0
        count = {}

        for right in range(len(s)):
            if s[right] in count:
                count[s[right]] += 1
            else:
                count[s[right]] = 1
            
            maxFreq = max(maxFreq, count[s[right]])

            if (right - left + 1) - maxFreq > k:
                count[s[left]] -= 1
                left += 1
            
            ans = max(ans, (right - left + 1))
        
        return ans
