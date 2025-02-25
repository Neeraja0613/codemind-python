t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    c=(x==0)+(y==0)+(z==0)
    if c>=2:
        print("WATER FILLING TIME")
    else:
        print("NOT NOW")
