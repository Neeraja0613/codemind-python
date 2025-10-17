# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    pos=n
    for i in range(1,n):
        if i%2==1:
            pos-=(n-i)
        else:
            pos+=(n-i)
    print(pos)
