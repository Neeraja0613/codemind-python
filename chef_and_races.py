# cook your dish here
t=int(input())
for i in range(t):
    x,y,a,b=map(int,input().split())
    if x!=a and x!=b and y!=a and y!=b:
        print("2")
    elif (x!=a and x!=b) or (y!=a and y!=b):
        print("1")
    else:
        print("0")
