t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    arr.sort(reverse=True)
    s=sum(arr[:k])
    print(s)
