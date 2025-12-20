class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        x=y=True
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                x=False
            if nums[i]<nums[i-1]:
                y=False
        return x or y
