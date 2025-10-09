class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        n=[]
        for i in range(left,right+1):
            r=[]
            for j in str(i):
                r.append(int(j))
            c=0
            for j in r:
                if j!=0 and i%j==0:
                    c+=1
            if len(r)==c:
                n.append(i)
        return n
