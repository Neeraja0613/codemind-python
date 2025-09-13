from collections import Counter
class Solution:
    def maxFreqSum(self, s: str) -> int:
        c=""
        d=""
        for i in s:
            if i in "aeiouAEIOU":
                c=c+i
            else:
                d=d+i
        a=Counter(c)
        b=Counter(d)
        x=max(a.values(),default=0)
        y=max(b.values(),default=0)
        return x+y
