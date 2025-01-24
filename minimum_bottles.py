# cook your dish here
t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    tot=sum(a)
    mini=(tot+x-1)//x
    print(mini)
