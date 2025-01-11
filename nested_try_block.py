try:
    num = int(input("Enter a number: "))
    try:
        result = 10 / num
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
except ValueError:
    print("Invalid input! Please enter a number.")
