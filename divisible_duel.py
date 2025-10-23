# cook your dish here
T = int(input())
for _ in range(T):
    X, Y = map(int, input().split())
    even_sum = 0
    odd_sum = 0
    for num in range(X, Y + 1):
        if num % X == 0:
            if num % 2 == 0:
                even_sum += num
            else:
                odd_sum += num
    print("YES" if even_sum >= odd_sum else "NO")
