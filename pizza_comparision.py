# cook your dish here
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    if(100/a>225/b):
        print("Small")
    elif(100/a==225/b):
        print("Equal")
    else:
        print("Large")
