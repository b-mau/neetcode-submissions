class Solution:
    def isHappy(self, n: int) -> bool:
        def next_num(x: int) -> int:
            total = 0
            while x:
                x, d = divmod(x, 10)
                total += d * d
            return total

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = next_num(n)
        return n == 1