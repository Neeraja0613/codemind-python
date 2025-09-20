class Solution:
    def countBits(self, n: int) -> List[int]:
        r=[]
        for i in range(n+1):
            x=bin(i)[2:]
            r.append(x.count('1'))
        return r
