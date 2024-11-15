# cook your dish here
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    min=10*n
    max=12*n
    if min<=k<=max:
        print("YES")
    else:
        print("NO")
