class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        r=[]
        for i in image:
            x=(i[::-1])
            n=[]
            for j in x:
                if j==0:
                    n.append(1)
                else:
                    n.append(0)
            r.append(n)
        return r
