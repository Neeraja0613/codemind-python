# Handling exceptions
try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ValueError:
    print("Invalid input. Please enter a number.")
except ZeroDivisionError:
    print("Division by zero is not allowed.")
