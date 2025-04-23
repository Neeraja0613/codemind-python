def max_tri(n):
    for i in range(n,2,-1):
        a,b,c=i-2,i-1,i
        if a+b>c:
            return a+b+c
    return -1

t=int(input())
for i in range(t):
    n=int(input())
    print(max_tri(n))
