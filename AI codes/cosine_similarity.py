# python version

import math

def cosine_similarity(v1,v2):
    dot = sum( a * b for a, b in zip(v1,v2))
    mag1 = math.sqrt(sum(a ** 2 for a in v1))
    mag2 = math.sqrt(sum(b ** 2 for b in v2))
    return dot / (mag1 * mag2)

def top_k(query_vec, doc_vecs, k):
    scores = [(cosine_similarity(query_vec, doc), doc) for doc in doc_vecs]
    scores.sort(reverse = True)
    return scores[:k]

# test it
v1 = [1, 2, 3]
v2 = [1, 2, 3]  # identical → should be 1.0
v3 = [0, 0, 1]  # different → lower

print(cosine_similarity(v1, v2))  # 1.0
print(cosine_similarity(v1, v3))  # lower



# numpy version

import numpy as np

def cosine_similarity_numpy(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

print(cosine_similarity_numpy(v1, v2))  # same 1.0
print(cosine_similarity_numpy(v1, v3))  # same lower number