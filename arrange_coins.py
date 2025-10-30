class Solution:
    def arrangeCoins(self, n: int) -> int:
        x=0
        while n>=x+1:
            x+=1
            n-=x
        return x
