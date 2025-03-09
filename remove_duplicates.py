def remove_duplicates(lst):
    return list(set(lst))

numbers = [int(x) for x in input("Enter numbers: ").split()]
print("List after removing duplicates:", remove_duplicates(numbers))
