t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    x=max(a)
    print(a.index(x)+1)
