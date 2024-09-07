from matrix_operations import matrix_addition, matrix_multiplication, matrix_inverse, matrix_transpose, matrix_determinant, generate_random_matrix, display_matrix
from eigenvectors import compute_eigenvalues, compute_eigenvectors, eigendecomposition, display_matrix, display_eigenvectors

def matrix_main():
    # Generating two random 2x2 matrices
    A = generate_random_matrix((3, 3))
    B = generate_random_matrix((3, 2))  # Incompatible size for testing error handling
    C = generate_random_matrix((3, 3))
    
    print("Matrix A:")
    print(A)
    display_matrix(A)
    
    print("Matrix B:")
    print(B)
    display_matrix(B)
    
    print("Matrix C:")
    print(C)
    display_matrix(C)
    
    # Matrix Addition
    print("\nMatrix Addition (A + C):")
    AC = matrix_addition(A, C)
    print(AC)
    display_matrix(AC)
    

    # Matrix Multiplication
    print("\nMatrix Multiplication (A * B):")
    AB = matrix_multiplication(A, B)
    print(AB)
    display_matrix(AB)

    # Matrix Inverse (if A is not singular)
    print("\nInverse of Matrix A:")
    IA = matrix_inverse(A)
    print(IA)
    display_matrix(IA)

    # Matrix Multiplication with Inverse (should return identity matrix)
    print("\nMatrix Multiplication with Inverse (A * A^-1):")
    I = matrix_multiplication(A, IA)
    print(I)
    display_matrix(I)

    # Matrix Transpose
    print("\nTranspose of Matrix A:")
    AT = matrix_transpose(A)
    print(AT)
    display_matrix(AT)

    # Matrix Determinant (should work if A is square)
    print("\nDeterminant of Matrix A:")
    print(matrix_determinant(A))

def eigenvectors_main():
    # Generating a random 3x3 matrix
    A = generate_random_matrix((3, 3))
    
    print("Matrix A:")
    print(A)
    display_matrix(A, title="Matrix A")
    
    # Compute eigenvalues and eigenvectors
    eigenvalues, eigenvectors = eigendecomposition(A)
    
    print("\nEigenvalues:")
    print(eigenvalues)

    print("\nEigenvectors:")
    print(eigenvectors)
    display_eigenvectors(A, eigenvectors, eigenvalues)  # Displaying both matrix and eigenvectors visually

def main():
    choice = input("Enter 1 for matrix operations and 2 for eigenvectors: ")
    match choice:
        case "1":
            matrix_main()
        case "2":
            eigenvectors_main()
        case _:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()