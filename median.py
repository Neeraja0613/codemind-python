class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
            x=sorted(nums1+nums2)
                n=len(x)
                if n%2==0:
                    a=n//2
                    return (x[a]+x[a-1])/2.0
                else:
                    a=n//2
                    return x[a]
