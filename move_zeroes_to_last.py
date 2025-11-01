class Solution:
    def pushZerosToEnd(self, arr):
        n=len(arr)
        c=0
        for i in range(n):
            if arr[i]!=0:
                arr[c]=arr[i]
                c+=1
        while c<n:
            arr[c]=0
            c+=1
