#Preconditions: linearly independent, equal dimensions vectors
import numpy as np

def gram_schmidt(vectors):
    size = len(vectors)
    orthonormal_vectors = []
    orthonormal_vectors.append(vectors[0] / np.linalg.norm(vectors[0]))
    for i in range(1, size):
        vector = vectors[i]
        #subtract vector's components in previous orthonormal_vector directions
        for j in range(i):
            vector = vector - np.dot(vector, orthonormal_vectors[j]) * orthonormal_vectors[j]
        vector = vector / np.linalg.norm(vector)
        orthonormal_vectors.append(vector)
    return orthonormal_vectors

def main():
    #test vectors here
    
    pass

if __name__ == '__main__':
    main()
    