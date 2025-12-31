class Solution:
    def checkDuplicatesWithinK(self, arr, k):
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if arr[i]==arr[j] and abs(i-j)<=k:
                    return True
        return False
