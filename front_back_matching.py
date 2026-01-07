# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    if n==1 or len(set(s))<n:
        print("YES")
    else:
        print("NO")
