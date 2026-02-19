# Verify configurations represented by the Gram matrix of sphere center vectors

import numpy as np
import argparse


# Define command-line arguments
parser = argparse.ArgumentParser()

parser.add_argument('--file-path', type=str, help='Path to the coordinate file')
parser.add_argument('--threshold', type=float, default=0.5, help='Cosine similarity threshold')
parser.add_argument('--atol', type=float, default=1e-6, help='Absolute tolerance for comparison')




def check_cosine_similarity(cosmatrix, threshold=0.5, atol=1e-6):
    """
    Check if pairwise cosine similarities in the matrix are less than or equal to threshold
    """
    
    # The diagonal elements should be equal to 1.0
    diag_mask = np.eye(cosmatrix.shape[0], dtype=bool)
    cosmatrix_diag = cosmatrix[diag_mask]
    is_diag_one = np.allclose(cosmatrix_diag, 1.0, atol=atol)
    print(f"Diagonal elements are equal to 1.0: {is_diag_one}")
    
    # Mask the diagonal elements and the rest should be less than or equal to to threshold
    cosmatrix_no_diag = cosmatrix[~diag_mask]
    is_off_diag_leq_threshold = np.all(cosmatrix_no_diag <= threshold + atol)
    print(f"All off-diagonal elements are less than or equal to {threshold}: {is_off_diag_leq_threshold}")
    
    # Cosine set of this configuration
    cosmatrix_no_diag_round = np.round(cosmatrix_no_diag, decimals=3)
    cos_set = np.unique(cosmatrix_no_diag_round)
    print(f"Cosine set: {cos_set}")
    
    
def check_positive_semi_definite(cosmatrix, atol=1e-6):
    """
    Check if the cosine matrix is positive semi-definite
    """
    
    eigenvalues = np.linalg.eigvalsh(cosmatrix)
    is_psd = np.all(eigenvalues >= -atol)
    print(f"Cosine matrix is positive semi-definite: {is_psd}")


def check_rank(cosmatrix):
    """
    Check the rank of cosine matrix 
    """
    
    rank = np.linalg.matrix_rank(cosmatrix)
    print(f"Rank of the cosine matrix: {rank}")
    
if __name__ == "__main__":
    args = parser.parse_args()
    coor = np.load(args.file_path)

    check_cosine_similarity(coor, threshold=args.threshold, atol=args.atol)
    check_positive_semi_definite(coor, atol=args.atol)
    # If you loads a n-dimensional configuration, the rank should be less than or equal to n
    check_rank(coor)