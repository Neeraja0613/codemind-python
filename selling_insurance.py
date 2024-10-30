# cook your dish here
t=int(input())
for i in range(t):
    x=int(input())
    if (100//(0.2*x))*(0.2*x)==100:
        print(int((100//(0.2*x))))
    else:
        print(int((100//(0.2*x)+1)))
