# Add a scalar to a matrix
A = np.array([[1, 2], [3, 4]])
print("A + 5:\n", A + 5)

# Broadcasting in operations
row = np.array([1, 2])
result = A + row
print("Broadcasting Result:\n", result)
