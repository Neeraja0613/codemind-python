# cook your dish here
t=int(input())
for i in range(t):
    w,p,k=map(int,input().split())
    wood=min(w,k)
    plas=k-wood
    print(2*wood+plas)
