import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = s.lower()
        new_s = re.sub(r'[^a-zA-Z0-9]', '', new_s)


        pointer1 = 0
        pointer2 = len(new_s) - 1

        while pointer1 < pointer2:
            if new_s[pointer1] == new_s[pointer2]:
                pointer1 += 1
                pointer2 -= 1
            else: 
                return False
        
        return True
        