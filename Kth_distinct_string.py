from collections import Counter
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        x=Counter(arr)
        r=[]
        for i in arr:
            if x[i]==1:
                r.append(i)
        if k<=len(r):
            return r[k-1]
        else:
            return ""
