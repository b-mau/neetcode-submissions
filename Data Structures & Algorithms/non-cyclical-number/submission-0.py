class Solution:
    def isHappy(self, n: int) -> bool:
        def next_num(x: int) -> int:
            total = 0
            while x:
                x, d = divmod(x,10)
                total += d*d
            return total
        
        slow, fast = n, next_num(n)
        while fast != 1 and slow != fast:
            slow  = next_num(slow)
            fast = next_num(next_num(fast))
        
        return fast == 1