class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        while len(nums)>1:
            r=[]
            for i in range(len(nums)-1):
                r.append((nums[i]+nums[i+1])%10)
            nums=r
        return nums[0]
