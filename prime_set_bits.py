class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        p={2,3,5,7,11,13,17,19,23,29,31}
        c=0
        for i in range(left,right+1):
            s=bin(i).count("1")
            if s in p:
                c+=1
        return c
