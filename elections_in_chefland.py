# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    c=0
    lst=list(map(int,input().split()))
    for j in lst:
        if j>=y:
            c+=1
    print(c)
