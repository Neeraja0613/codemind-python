class Solution:
    def majorityElement(self, arr):
        #code here
        dict={}
        n=len(arr)
        for i in arr:
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1
        for i in dict:
            if dict[i]>n//2:
                return i
        return -1
