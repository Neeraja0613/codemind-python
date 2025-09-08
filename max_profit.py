class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        m=prices[0]
        for i in range(1,len(prices)):
            m=min(m,prices[i])
            res=max(res,prices[i]-m)
        return res
