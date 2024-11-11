def maximum_69_number(num):
    # Convert the number to a string to modify the digits
    num_str = str(num)
    
    # Iterate over the digits to find the first occurrence of '6'
    for i in range(len(num_str)):
        if num_str[i] == '6':
            # Change the first '6' to '9' and break the loop
            num_str = num_str[:i] + '9' + num_str[i+1:]
            break
    
    # Convert back to integer and return
    return int(num_str)

# Main code
if _name_ == "_main_":
    # Read the integer input
    N = int(input())
    
    # Get the maximum number
    result = maximum_69_number(N)
    
    # Output the result
    print(result)
