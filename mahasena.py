n=int(input())
lst=list(map(int,input().split()))
c=0
cnt=0
for i in range(n):
    if lst[i]%2==0:
        c=c+1
    else:
        cnt=cnt+1
if c>cnt:
    print("READY FOR BATTLE")
else:
    print("NOT READY")
