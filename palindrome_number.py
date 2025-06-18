class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        n=str(x)[::-1]
        return x==int(n)
