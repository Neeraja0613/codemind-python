class Solution:
    def guessNumber(self, n: int) -> int:
        l=1
        h=n
        while l<=h:
            m=l+(h-l)//2
            r=guess(m)
            if r==0:
                return m
            elif r<0:
                h=m-1
            else:
                h=m+1
