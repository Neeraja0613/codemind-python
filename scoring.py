t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    A=(y+x)//2
    B=(y-x)//2
    print(A,B)
