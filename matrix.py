# Dot product
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
dot_product = np.dot(A, B)
print("Dot Product:\n", dot_product)

# Transpose
print("Transpose of A:\n", A.T)

# Inverse
from numpy.linalg import inv
print("Inverse of A:\n", inv(A))
