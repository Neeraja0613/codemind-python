def is_triangular(num):
    # Function to check if a number is triangular
    n = 1
    while (n * (n + 1)) // 2 <= num:
        if (n * (n + 1)) // 2 == num:
            return True
        n += 1
    return False

def calculate_money(weights, N, K):
    total_sum = 0
    for weight in weights:
        if not is_triangular(weight):
            total_sum += weight
    return total_sum

# Example usage
weights = [10, 6, 5, 15, 21]
N = 3
K = 2
print(calculate_money(weights, N, K))  # Output will be 5
