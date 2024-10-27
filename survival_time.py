# cook your dish here
t=int(input())
for i in range(t):
    n,x,d=map(int,input().split())
    print(n//(5*x)+d)
