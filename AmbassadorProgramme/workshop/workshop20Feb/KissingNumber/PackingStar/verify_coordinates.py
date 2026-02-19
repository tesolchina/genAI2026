# Verify configurations represented by sphere center coordinates

import numpy as np
import argparse

# Define command-line arguments
parser = argparse.ArgumentParser()

parser.add_argument('--file-path', type=str, help='Path to the coordinate file')
parser.add_argument('--threshold', type=float, default=0.5, help='Cosine similarity threshold')
parser.add_argument('--atol', type=float, default=1e-6, help='Absolute tolerance for comparison')
parser.add_argument('--batch-size', type=int, default=3000, help='Batch size for processing')


def check_cosine_similarity_batch(coor, threshold=0.5, atol=1e-6, batch_size=3000):
    """
    Check if pairwise cosines of sphere center vectors are less than or equal to threshold
    """
    
    # Normalize the coordinate vectors
    norms = np.linalg.norm(coor, axis=1, keepdims=True)
    coor_normalized = coor / norms 
    
    # Divide into batches to avoid memory issues
    n = coor_normalized.shape[0]
    print(f"Total vectors: {n}, Batch size: {batch_size}")    
    all_less_than_threshold = True    
    cos_set = set()

    for i in range(0, n, batch_size):
        end_i = min(i + batch_size, n)
        current_batch = coor_normalized[i:end_i]
        
        # Calculate cosine similarities for the current batch
        batch_similarity = current_batch @ coor_normalized.T
        
        # Create a mask to exclude diagonal elements (self-similarity)
        batch_size_current = batch_similarity.shape[0]
        mask = np.ones(batch_similarity.shape, dtype=bool)
        
        # Logic: The j-th row of the current batch corresponds to the global index i+j
        # so we need to mask the i+j-th column
        for j in range(batch_size_current):
            if i + j < n:
                mask[j, i + j] = False
        
        valid_similarities = batch_similarity[mask]
        
        # Check if the current batch meets the constraint
        has_violation = np.any(valid_similarities > threshold + atol)
        
        # Maintain a set for cosine values
        valid_similarities_round = np.round(valid_similarities, decimals=6)
        unique_vals = np.unique(valid_similarities_round)
        cos_set.update(unique_vals.tolist())
        
        if has_violation:
            print(f"Found violations in batch starting at index {i}")
            all_less_than_threshold = False
            break
        
        # Cleanup
        del batch_similarity, mask, valid_similarities
        
        print(f"Processed batch {i//batch_size + 1}/{(n+batch_size-1)//batch_size}")

    return all_less_than_threshold, cos_set


if __name__ == "__main__":
    args = parser.parse_args()
    coor = np.load(args.file_path)
    
    result, cos_set = check_cosine_similarity_batch(coor, threshold=args.threshold, atol=args.atol, batch_size=args.batch_size)
    print("Is all cosine value less than {}: {}".format(args.threshold, result))
    print("Cosine set:", cos_set)
