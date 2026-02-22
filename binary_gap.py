class Solution:
    def binaryGap(self, n: int) -> int:
        b=bin(n)[2:]
        p=[i for i,bit in enumerate(b) if bit=='1']
        if len(p)<2:
            return 0
        x=max(p[i+1]-p[i] for i in range(len(p)-1))
        return x
