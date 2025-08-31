from itertools import combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        r=[]
        for i in range(len(nums)+1):
            r.extend(combinations(nums,i))
        return [list(i) for i in r]
