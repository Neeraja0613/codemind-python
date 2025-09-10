r,b=map(int,input().split())
g=min(r,b)
rr=r-g
rb=b-g
s=rr*1+rb*2+g*5
print(s)
