t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    res=(a+b)/2
    if res>c:
        print("YES")
    else:
        print("NO")
