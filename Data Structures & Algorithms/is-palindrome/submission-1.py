import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new_str = ""
        for char in s:
            if char.isalnum():
                new_str += char
            else: 
                continue
        print(new_str)
        pointer1 = 0
        pointer2 = len(new_str) - 1
        
        while pointer1 < pointer2:
            if new_str[pointer1] != new_str[pointer2]:
                return False
            pointer1 += 1
            pointer2 -= 1
        
        return True