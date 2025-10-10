class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        c = 0
        for i in range(len(t)):
            if c<len(s) and t[i]==s[c]:
                c = c+1
        return len(s)==c
