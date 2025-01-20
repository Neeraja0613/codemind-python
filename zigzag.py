n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    for j in range(1, 2 * n):
        if (i + j) % 4 == 0 or (i == 2 and j % 4 == 0):
            print("*", end="")
        else:
            print(" ", end="")
    print()
