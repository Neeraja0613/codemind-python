from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        s=0
        x=Counter(nums)
        r=max(x.values())
        for i in x.values():
            if i==r:
                s+=i
        return s
            
