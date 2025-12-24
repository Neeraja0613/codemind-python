# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    s=0
    for i in range(1,n+1):
        s+=i*a[i-1]
    print(s)
