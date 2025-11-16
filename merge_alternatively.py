class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        r=[]
        i,j=0,0
        l1,l2=len(word1),len(word2)
        while i<l1 or j<l2:
            if i<l1:
                r.append(word1[i])
                i+=1
            if j<l2:
                r.append(word2[j])
                j+=1
        return ''.join(r)
