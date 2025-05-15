t=int(input())
for i in range(t):
    n=int(input())
    min_cost=float('inf')
    for j in range(n):
        x,y=map(int,input().split())
        if x>=7:
            min_cost=min(min_cost,y)
    if min_cost!=float('inf'):
        print(min_cost)
    else:
        print("-1")
