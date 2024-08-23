n=int(input())
arr=list(map(int,input().split()))
for i in range(n):
     if arr[i]%2==0:
          print(arr[i])
for i in range(n):
     if arr[i]%2==1:
          print(arr[i])
