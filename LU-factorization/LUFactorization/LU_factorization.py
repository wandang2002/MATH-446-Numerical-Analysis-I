import random 
import numpy as np
from typing import Tuple
np.set_printoptions(formatter={'float_kind':'{:.2f}'.format})
def special_matrices(n:int, rand:int) -> np.ndarray: 
    random.seed(rand)
    A = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            if abs(i-j) <= 1:
                A[i,j] = random.randint(1,10)
            else:
                continue
    return A

def gauss_for_special_matrices(A:np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    # Get the size of the matrix
    n = A.shape[0]
    # Initialize the lower triangular matrix
    L = np.zeros((n,n))
    L[0,0] = 1
    # Perform the Gaussian elimination for special matrices
    for i in range(1, n):
        # Compute the multiplier
        multiplier = A[i,i-1]/A[i-1,i-1]
        # Update the lower triangular matrix
        L[i,i-1] = multiplier
        L[i,i] = 1
        # Update the matrix A
        A[i,i-1] = 0
        A[i,i] = A[i,i] - multiplier*A[i-1,i]   
    U = A
    return L, U

def generate_random_vectors(n:int, rand:int) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    random.seed(rand)
    a = np.array([random.randint(1,10) for i in range(n)])
    b = np.array([random.randint(1,10) for i in range(n-1)])
    c = np.array([random.randint(1,10) for i in range(n-1)])
    a, b, c = a.astype(float), b.astype(float), c.astype(float)
    return a, b, c
    
def gauss_for_special_matrices_less_memory(a, b, c: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    if (len(b) != len(c)) and (len(a) != len(b)-1):
        raise ValueError("The length of the vectors are not compatible.")
    # Get the size of the matrix
    n = len(a)
    # Initialize the lower triangular matrix
    L = np.zeros((n,n))
    L[0,0] = 1
    # Initalize the upper triangular matrix
    U = np.zeros((n,n))
    # Perform the Gaussian elimination for special matrices
    for i in range(0, n-1):
        # Compute the multiplier
        multiplier = c[i]/a[i]
        # Update the lower triangular matrix
        L[i+1,i] = multiplier
        L[i+1,i+1] = 1
        # Update the vector 
        c[i] = 0
        a[i+1] = a[i+1] - multiplier*b[i]
    return L, a, b , c

def generate_matrix(a,b,c):
    n = len(a)
    U = np.zeros((n,n))
    for i in range(n):
        U[i,i] = a[i]
        if i < n-1:
            U[i,i+1] = b[i]
            U[i+1,i] = c[i]
    return U



