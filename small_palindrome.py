# cook your dish here
t=int(input())
for i in range(t):
    def smallest_palindrome(x,y):
        a="1"*(x// 2)+"2"*(y//2)
        p=a+a[::-1]
        print(p)
    x,y=map(int,input().split())
    smallest_palindrome(x,y)
