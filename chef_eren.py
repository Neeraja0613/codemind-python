# cook your dish here
t=int(input())
for i in range(t):
    n,a,b=map(int,input().split())
    c1=0
    c2=0
    for j in range(1,n+1):
        if j%2==0:
            c1+=1
        else:
            c2+=1
    print((a*c1)+(b*c2))
