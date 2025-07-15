from collections import Counter
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        c=Counter(nums)
        for i in range(len(nums)):
            if c[nums[i]]==1:
                return nums[i]
