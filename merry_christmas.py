# cook your dish here
act=[1,2,4]
x=int(input())
c=0
for i in act:
    if x>=i:
        x-=i
        c+=1
    else:
        break
print(c)
