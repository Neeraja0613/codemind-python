# cook your dish here
import math
t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    sub=math.ceil(n/6)
    res=sub*x
    print(res)
