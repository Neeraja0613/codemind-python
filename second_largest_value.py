class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        x=list(set(arr))
        if len(x)<2:
            return -1
        x.remove(max(x))
        return max(x)
                
