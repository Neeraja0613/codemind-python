class Solution:
    def reverseBits(self, n: int) -> int:
        x=bin(n)[2:].zfill(32)
        y=x[::-1]
        return int(y,2)
