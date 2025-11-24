class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        c=""
        r=[]
        for i in nums:
            c=c+str(i)
            a=int(c,2)
            if a%5==0:
                r.append(True)
            else:
                r.append(False)
        return r
