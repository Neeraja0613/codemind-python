#User function Template for python3
from collections import Counter
class Solution:
    def singleNum(self, arr):
        # Code here
        r=[]
        x=Counter(arr)
        for i in range(len(arr)):
            if x[arr[i]]==1:
                r.append(arr[i])
        return sorted(r)
