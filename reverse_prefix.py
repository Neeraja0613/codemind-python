class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        x=word.index(ch)
        p=word[:x+1][::-1]
        s=word[x+1:]
        return p+s
