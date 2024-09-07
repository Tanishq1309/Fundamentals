import numpy as np
import matplotlib.pyplot as plt

# Function to compute eigenvalues of a matrix
def compute_eigenvalues(A):
    """Computes the eigenvalues of matrix A."""
    try:
        return np.linalg.eigvals(A)
    except Exception as e:
        return f"Error: {e}"

# Function to compute eigenvectors of a matrix
def compute_eigenvectors(A):
    """Computes the eigenvectors of matrix A."""
    try:
        _, eigenvectors = np.linalg.eig(A)
        return eigenvectors
    except Exception as e:
        return f"Error: {e}"

# Function to perform both eigenvalue and eigenvector decomposition
def eigendecomposition(A):
    """Performs eigendecomposition on matrix A, returning eigenvalues and eigenvectors."""
    try:
        eigenvalues, eigenvectors = np.linalg.eig(A)
        return eigenvalues, eigenvectors
    except Exception as e:
        return f"Error: {e}"

# Display matrix visually
def display_matrix(A, title="Matrix"):
    """Displays the matrix A in a visually appealing way using matplotlib."""
    try:
        fig, ax = plt.subplots()
        ax.set_axis_off()

        # Render matrix as a table
        table = ax.table(cellText=np.round(A, decimals=2), loc='center', cellLoc='center', edges='closed')
        
        # Customize table appearance (optional)
        table.auto_set_font_size(False)
        table.set_fontsize(14)
        table.scale(1.5, 1.5)  # Adjust scale for better readability

        ax.set_title(title, fontsize=16)
        
        plt.show()

    except Exception as e:
        return f"Error: {e}"

# Helper function to format matrices as simple strings
def matrix_to_string(A):
    """Formats a matrix as a string for display."""
    return "\n".join(["[" + "  ".join([f"{elem:.2f}" for elem in row]) + "]" for row in A])

# Function to display the equation Av = lambda * v with proper visualization
def display_eigenvectors(A, eigenvectors, eigenvalues):
    """Displays the equation A * v = lambda * v for each eigenvector."""
    try:
        # Loop through each eigenvector and eigenvalue
        for i in range(eigenvectors.shape[1]):
            v_i = eigenvectors[:, i]  # The i-th eigenvector
            lambda_i = eigenvalues[i]  # The i-th eigenvalue
            
            # Compute A * v_i
            Av_i = np.dot(A, v_i)
            
            # Start the figure for visualizing the equation
            fig, ax = plt.subplots(figsize=(12, 5))

            # Remove axes for clean visualization
            ax.set_axis_off()

            # Display the matrix A
            A_text = f"Matrix A:\n{matrix_to_string(A)}"

            # Display the eigenvector v_i
            v_text = f"Eigenvector v_{i+1}:\n[{', '.join([f'{val:.2f}' for val in v_i])}]"

            # Display A * v_i result
            Av_text = f"A * v_{i+1}:\n[{', '.join([f'{val:.2f}' for val in Av_i])}]"

            # Display lambda * v_i result
            lambda_v_text = f"λ_{i+1} * v_{i+1} = {lambda_i:.2f} * [{', '.join([f'{val:.2f}' for val in v_i])}]"

            # Add the text to the plot
            ax.text(0.1, 0.8, A_text, fontsize=14, verticalalignment='top', horizontalalignment='left')
            ax.text(0.55, 0.8, v_text, fontsize=14, verticalalignment='top', horizontalalignment='left')
            ax.text(0.1, 0.4, Av_text, fontsize=14, verticalalignment='top', horizontalalignment='left')
            ax.text(0.55, 0.4, lambda_v_text, fontsize=14, verticalalignment='top', horizontalalignment='left')

            plt.suptitle(f"Eigenvalue {lambda_i:.2f} and Eigenvector {i+1}", fontsize=16)
            plt.show()

    except Exception as e:
        return f"Error: {e}"