class Solution:
    def mergeArrays(self, a, b):
        x=len(a)
        n=sorted(a+b)
        a[:]=n[:x]
        b[:]=n[x:]
        return a,b
