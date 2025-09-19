t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    s=input()
    a=s.count('1')
    b=s.count('0')
    r=n-m
    diff=b+r-a
    if diff%2==0 and 0<=diff//2<=r:
        print("YES")
    else:
        print("NO")
