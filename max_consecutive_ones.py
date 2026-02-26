class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c=0
        d=[]
        for i in range(len(nums)):
            if nums[i]==0:
                d.append(c)
                c=0
            else:
                c=c+1
        d.append(c)
        return max(d)
