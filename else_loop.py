# prime or not
# trying to run a loop from 2 to n-1
n=int(input())
is_prime=True
for i in range(2,n):
    if n%i==0:
        is_prime=False
        break
if is_prime==True:
    print("Prime")
else:
    print("Not Prime")
