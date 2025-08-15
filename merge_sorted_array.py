class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        r1=nums1[:m]
        r2=nums2[:n]
        res=sorted(r1+r2)
        for i in range(len(res)):
            nums1[i]=res[i]
