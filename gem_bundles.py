# cook your dish here
t=int(input())
for i in range(t):
    r,b,g=map(int,input().split())
    x=min(r,b,g)
    a=x*10
    b=r+b+g-3*x 
    c=b*3 
    print(a+c)
