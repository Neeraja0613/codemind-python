# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    print(abs((y-1)//10-(x-1)//10))
