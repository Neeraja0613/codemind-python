class Solution:
    def convertToTitle(self, n: int) -> str:
        r=""
        while n>0:
            n-=1
            r=chr(n%26 + ord('A'))+r
            n//=26
        return r
