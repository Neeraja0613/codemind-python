numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]
numbers.sort()
print("Sorted List (Ascending):", numbers)

numbers.sort(reverse=True)
print("Sorted List (Descending):", numbers)
