class Solution:
    def findExtra(self,a,b):
        #add code here
        for i in a:
            if i not in b:
                return a.index(i)
