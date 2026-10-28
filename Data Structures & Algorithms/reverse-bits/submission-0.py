class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            result = (result << 1) | (n & 1)  # make room, then add n's lowest bit
            n >>= 1                           # move on to n's next bit
        return result