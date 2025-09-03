class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        c=0
        x=word
        while x in sequence:
            c+=1
            x+=word
        return c
