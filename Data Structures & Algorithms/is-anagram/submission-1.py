class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1 = {}
        for char in s:
            if char not in hash1.keys():
                hash1[char] = 1
            else:
                hash1[char] += 1
        
        hash2 = {}
        for char in t:
            if char not in hash2.keys():
                hash2[char] = 1
            else:
                hash2[char] += 1
        
        return hash1 == hash2
