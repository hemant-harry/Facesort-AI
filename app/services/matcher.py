import numpy as np

def compare_faces(embedding1, embedding2, threshold=0.65):
    """
    Compare two face embeddings using cosine similarity.
    Returns:
        is_match (bool)
        similarity (float)
    """

    similarity = np.dot(embedding1, embedding2) / (
        np.linalg.norm(embedding1) * np.linalg.norm(embedding2)
    )

    similarity = float(similarity)

    return similarity >= threshold, similarity