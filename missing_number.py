class Solution:
    def missingNum(self, arr):
        # code here
        n=len(arr)+1
        tot=n*(n+1)//2
        arr_sum=sum(arr)
        return tot-arr_sum
