# cook your dish here
t=int(input())
for i in range(t):
    n,x,k=map(int,input().split())
    r=x%k
    a=r
    b=k-r if x+(k-r)<=n else float('inf')
    print(min(a,b))
