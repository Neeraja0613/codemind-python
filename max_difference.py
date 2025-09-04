class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        mini=nums[0]
        maxi=-1
        for i in range(1,len(nums)):
            if nums[i]>mini:
                maxi=max(maxi,nums[i]-mini)
            else:
                mini=nums[i]
        return maxi
