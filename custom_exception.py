class NegativeNumberError(Exception):
    """Exception raised for negative numbers."""
    pass

def check_number(num):
    if num < 0:
        raise NegativeNumberError("Negative numbers are not allowed!")
    return num

try:
    number = int(input("Enter a positive number: "))
    print(f"Valid number: {check_number(number)}")
except NegativeNumberError as e:
    print(f"Error: {e}")
