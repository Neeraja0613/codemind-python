# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    if n%10>=5:
        x=((n//10)+1)*10
    else:
        x=(n//10)*10
    print(100-x)
