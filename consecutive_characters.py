class Solution:
    def maxPower(self, s: str) -> int:
        c=1
        r=[]
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                c+=1
            else:
                r.append(c)
                c=1
        r.append(c)
        return max(r)
