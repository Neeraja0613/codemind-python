a,b=map(int,input().split())
res=((a+1)*4)+(b*3)
if res%8==0:
    print(res//8)
else:
    print(res//8+1)
