class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        r=[]
        for idx, i in enumerate(words):
            if x in i:
                r.append(idx)
        return r
