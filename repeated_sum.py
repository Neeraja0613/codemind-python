class Solution:
    def repeatedSumOfDigits (self,n):
        # code here 
        while n>=10:
            s=0
            while n>0:
                r=n%10
                s+=r
                n//=10
            n=s
        return s
