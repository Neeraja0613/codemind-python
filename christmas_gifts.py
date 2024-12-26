# cook your dish here
t=int(input())
for i in range(t):
    h,l,w=map(int,input().split())
    area=2*((h*l)+(l*w)+(w*h))
    t_area=1000
    if area>0:
        maxi=t_area//area
    else:
        maxi=0
    print(maxi)
