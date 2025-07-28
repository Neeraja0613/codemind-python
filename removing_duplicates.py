class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x=sorted(set(nums))
        for i in range(len(x)):
            nums[i]=x[i]
        y=len(x)
        return y
