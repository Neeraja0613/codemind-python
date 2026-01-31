class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        r=[]
        for i in sentences:
            x=i.split()
            r.append(len(x))
        return max(r)
