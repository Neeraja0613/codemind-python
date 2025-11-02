# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    a=1500-6*x-4*y
    b=1500-2*x-6*y
    print(max(a,b))
