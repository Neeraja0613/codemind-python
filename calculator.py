# A simple calculator program
def calculator():
    print("Options: add, subtract, multiply, divide")
    operation = input("Enter the operation: ").lower()

    if operation in ["add", "subtract", "multiply", "divide"]:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if operation == "add":
            print("Result:", num1 + num2)
        elif operation == "subtract":
            print("Result:", num1 - num2)
        elif operation == "multiply":
            print("Result:", num1 * num2)
        elif operation == "divide":
            if num2 != 0:
                print("Result:", num1 / num2)
            else:
                print("Error: Division by zero")
    else:
        print("Invalid operation")

calculator()
