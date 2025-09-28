class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        a=bin(n)[2:]
        x=a[::-1]
        ec=oc=0
        for i in range(len(x)):
            if i%2==0 and x[i]=='1':
                ec+=1
            if i%2==1 and x[i]=='1':
                oc+=1
        return ec,oc
