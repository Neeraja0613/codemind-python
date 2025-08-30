class Solution:
    def hammingWeight(self, n: int) -> int:
        c=0
        binary=bin(n)[2:]
        for i in binary:
            if i=="1":
                c+=1
        return c
