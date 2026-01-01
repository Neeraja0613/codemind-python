class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        x=min(nums)
        y=max(nums)
        r=[]
        for i in range(x,y+1):
            if i not in nums:
                r.append(i)
        return r
