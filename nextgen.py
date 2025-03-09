def will_get_funding(A, B, X, Y):
    required_power = A * B
    available_power = X * Y
    return "YES" if available_power >= required_power else "NO"

t=int(input())
for i in range(t):
    A, B, X, Y = map(int, input().split())
    print(will_get_funding(A, B, X, Y))
