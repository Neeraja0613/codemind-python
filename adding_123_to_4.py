# cook your dish here
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    r=min(x,z)+(y//2)
    print(r)
