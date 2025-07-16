t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    c=0
    flag=True
    for j in range(1,n+1):
        c+=a[j-1]
        avg=c/j
        if avg<40:
            flag=False
    if flag:
        print("YES")
    else:
        print("NO")
