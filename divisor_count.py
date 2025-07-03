t=int(input())
for i in range(t):
    n=int(input())
    ec=0
    oc=0
    for j in range(1,n+1):
        if n%j==0:
            if j%2==0:
                ec+=1
            else:
                oc+=1
    print(oc,ec)
