t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    if z>((x*y)//2):
        print("YES")
    else:
        print("NO")
