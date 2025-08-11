class Solution:

    def kthElement(self, a, b, k):
        for i in range(len(b)):
            a.append(b[i])
        a.sort()
        return a[k-1]
