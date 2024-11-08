# cook your dish here
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    if y%z==0:
        print((y//z)*x)
    else:
        print(((y//z)+1)*x)
