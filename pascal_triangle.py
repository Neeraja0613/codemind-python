n = int(input("Enter the number of rows: "))
for i in range(n):
    print(" " * (n - i), end="")
    num = 1
    for j in range(i + 1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1)
    print()
