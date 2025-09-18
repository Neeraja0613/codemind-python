t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    x=n*k
    h=x//60
    m=x%60
    print(h,m)
