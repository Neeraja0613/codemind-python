import numpy as np

# Create a 1D array
arr1 = np.array([1, 2, 3, 4])
print("1D Array:", arr1)

# Create a 2D array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", arr2)

# Create arrays with specific values
zeros = np.zeros((2, 3))  # 2x3 array of zeros
ones = np.ones((3, 2))    # 3x2 array of ones
identity = np.eye(3)      # 3x3 identity matrix

print("Zeros:\n", zeros)
print("Ones:\n", ones)
print("Identity Matrix:\n", identity)
