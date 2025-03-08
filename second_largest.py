def second_largest(numbers):
    unique_numbers = list(set(numbers))  # Remove duplicates
    unique_numbers.sort(reverse=True)    # Sort in descending order
    return unique_numbers[1] if len(unique_numbers) > 1 else None

nums = [int(x) for x in input("Enter numbers: ").split()]
result = second_largest(nums)
print("Second Largest Number:", result if result is not None else "Not enough unique numbers")
