t=int(input())
for i in range(t):
    n=int(input())
    x=list(map(int,input().split()))
    osum=sum(x[i] for i in range(0,n,2))  
    esum=sum(x[i] for i in range(1,n,2))
    print(max(osum,esum))
