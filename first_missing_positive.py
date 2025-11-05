class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        x=set(nums)
        i=1
        while True:
            if i not in x:
                return i
            i+=1
