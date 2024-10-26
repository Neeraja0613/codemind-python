# cook your dish here
t=int(input())
for i in range(t):
    n,k,m=map(int,input().split())
    print((n+k*m-1)//(k*m))
