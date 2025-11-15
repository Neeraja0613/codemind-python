from collections import Counter
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        a=[]
        for i in nums:
            if i%2==0:
                a.append(i)
        if not a:
            return -1
        x=Counter(a)
        y=max(x.values())
        r=[]
        for i in a:
            if x[i]==y:
                r.append(i)
        return min(r)
