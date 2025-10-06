from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        x=Counter(s)
        for idx,i in enumerate(s):
            if x[i]==1:
                return idx
        return -1
