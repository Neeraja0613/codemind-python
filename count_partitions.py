class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        t=sum(nums)
        l=0
        c=0
        for i in range(len(nums)-1):
            l+=nums[i]
            r=t-l
            if l%2==r%2:
                c+=1
        return c
