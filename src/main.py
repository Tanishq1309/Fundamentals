import matrix_operations as matx
import eigenvectors as eig

def matrix_main():
    # Generating two random 2x2 matrices
    A = matx.generate_random_matrix((3, 3))
    B = matx.generate_random_matrix((3, 2))  # Incompatible size for testing error handling
    C = matx.generate_random_matrix((3, 3))
    
    print("Matrix A:")
    print(A)
    matx.display_matrix(A)
    
    print("Matrix B:")
    print(B)
    matx.display_matrix(B)
    
    print("Matrix C:")
    print(C)
    matx.display_matrix(C)
    
    # Matrix Addition
    print("\nMatrix Addition (A + C):")
    AC = matx.matrix_addition(A, C)
    print(AC)
    matx.display_matrix(AC)
    

    # Matrix Multiplication
    print("\nMatrix Multiplication (A * B):")
    AB = matx.matrix_multiplication(A, B)
    print(AB)
    matx.display_matrix(AB)

    # Matrix Inverse (if A is not singular)
    print("\nInverse of Matrix A:")
    IA = matx.matrix_inverse(A)
    print(IA)
    matx.display_matrix(IA)

    # Matrix Multiplication with Inverse (should return identity matrix)
    print("\nMatrix Multiplication with Inverse (A * A^-1):")
    I = matx.matrix_multiplication(A, IA)
    print(I)
    matx.display_matrix(I)

    # Matrix Transpose
    print("\nTranspose of Matrix A:")
    AT = matx.matrix_transpose(A)
    print(AT)
    matx.display_matrix(AT)

    # Matrix Determinant (should work if A is square)
    print("\nDeterminant of Matrix A:")
    print(matx.matrix_determinant(A))

def eigenvectors_main():
    # Generating a random 3x3 matrix
    A = matx.generate_random_matrix((3, 3))
    
    print("Matrix A:")
    print(A)
    eig.display_matrix(A, title="Matrix A")
    
    # Compute eigenvalues and eigenvectors
    eigenvalues, eigenvectors = eig.eigendecomposition(A)
    
    print("\nEigenvalues:")
    print(eigenvalues)

    print("\nEigenvectors:")
    print(eigenvectors)
    eig.display_eigenvectors(A, eigenvectors, eigenvalues)  # Displaying both matrix and eigenvectors visually

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