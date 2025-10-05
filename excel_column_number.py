class Solution:
    def titleToNumber(self, s: str) -> int:
        r=0
        for i in s:
            r=r*26+(ord(i)-ord('A')+1)
        return r
