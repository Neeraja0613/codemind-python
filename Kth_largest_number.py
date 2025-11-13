class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        r=[]
        for i in nums:
            r.append(int(i))
        x=sorted(r)[::-1]
        return str(x[k-1])
