while True:
    try:
        num = int(input("Enter a number (or type '0' to exit): "))
        if num == 0:
            break
        print(f"Result: {10 / num}")
    except ValueError:
        print("Invalid input! Please enter a valid number.")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
