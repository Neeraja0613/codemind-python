from itertools import permutations
class Solution:
    def findPermutation(self, s):
        r=[]
        p=permutations(s)
        for i in p:
            r.append(''.join(i))
        return sorted(set(r))
