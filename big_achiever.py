# cook your dish here
t=int(input())
for j in range(t):
    n=int(input())
    A=list(map(int, input().split()))
    maxi=0
    res=[]
    for i in range(n):
        if A[i]>maxi:
            res.append("1")
            maxi=A[i]
        else:
            res.append("0")
    print(" ".join(res))
