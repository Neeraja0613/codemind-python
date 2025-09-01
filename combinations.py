from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        r=[]
        for i in combinations(range(1,n+1),k):
            r.append(list(i))
        return r
