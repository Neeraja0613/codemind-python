# cook your dish here
t=int(input())
for i in range(t):
    n,k,x,y=map(int,input().split())
    if x<y:
        print(n*x)
    else:
        print((k*x)+(n-k)*y)
