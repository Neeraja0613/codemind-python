# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    if n%7>=2:
        x=(n//7)+1
    else:
        x=n//7
    print(x)
