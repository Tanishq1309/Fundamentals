import numpy as np
import matplotlib.pyplot as plt

# Matrix addition
def matrix_addition(A, B):
    """Adds two matrices A and B element-wise, checks if dimensions match."""
    try:
        if A.shape != B.shape:
            raise ValueError("Matrices must have the same dimensions for addition.")
        return np.add(A, B)
    except Exception as e:
        return f"Error: {e}"

# Matrix multiplication
def matrix_multiplication(A, B):
    """Multiplies two matrices A and B, checks if dimensions are compatible."""
    try:
        if A.shape[1] != B.shape[0]:
            raise ValueError("Matrices must have compatible dimensions for multiplication.")
        return np.matmul(A, B)
    except Exception as e:
        return f"Error: {e}"

# Matrix inverse
def matrix_inverse(A):
    """Returns the inverse of matrix A, checks if matrix is square and invertible."""
    try:
        if A.shape[0] != A.shape[1]:
            raise ValueError("Matrix must be square to compute the inverse.")
        return np.linalg.inv(A)
    except np.linalg.LinAlgError:
        return "Error: Matrix is singular and cannot be inverted."
    except Exception as e:
        return f"Error: {e}"

# Matrix transpose
def matrix_transpose(A):
    """Returns the transpose of matrix A."""
    try:
        return np.transpose(A)
    except Exception as e:
        return f"Error: {e}"

# Matrix determinant
def matrix_determinant(A):
    """Returns the determinant of matrix A, checks if matrix is square."""
    try:
        if A.shape[0] != A.shape[1]:
            raise ValueError("Matrix must be square to compute the determinant.")
        return np.linalg.det(A)
    except Exception as e:
        return f"Error: {e}"

# Generating a random matrix
def generate_random_matrix(size, low=-99, high=99):
    """Generates a random matrix of given size with values between low and high."""
    try:
        if not isinstance(size, tuple) or len(size) != 2:
            raise ValueError("Size must be a tuple of two integers (rows, columns).")
        return np.random.randint(low, high, size=size)
    except Exception as e:
        return f"Error: {e}"

# Display matrix visually
def display_matrix(A):
    """Displays the matrix A in a visually appealing way using matplotlib."""
    try:
        fig, ax = plt.subplots()
        ax.set_axis_off()

        # Render matrix as a table
        table = ax.table(cellText=A, loc='center', cellLoc='center', edges='closed')
        
        # Customize table appearance (optional)
        table.auto_set_font_size(False)
        table.set_fontsize(14)
        table.scale(1.5, 1.5)  # Adjust scale for better readability
        
        plt.show()

    except Exception as e:
        return f"Error: {e}"