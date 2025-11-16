from collections import Counter
class Solution:
    def countSpecials(self, k, arr):
        c=0
        n=len(arr)//k
        x=Counter(arr)
        for i in x:
            if x[i]==n:
                c+=1
        return c
