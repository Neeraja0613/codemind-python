import math
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        x=min(nums)
        y=max(nums)
        return math.gcd(x,y)
