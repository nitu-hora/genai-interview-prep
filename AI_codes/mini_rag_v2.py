from sentence_transformers import SentenceTransformer
from sentence_transformers import util

text = """Machine learning is a way of making computers learn from data.
Deep learning uses neural networks with many layers.
Transformers are the architecture behind GPT and BERT.
Self-supervised learning creates labels from the data itself.
RAG combines retrieval with generation to asnwer questions."""

model = SentenceTransformer("all-MiniLM-L6-v2")
print("model loaded")

def chunk_text(text):
    return [s.strip() for s in text.split(".") if s.strip() != ""]

chunks = chunk_text(text)
chunk_embeddings = model.encode(chunks)

print("number of chunks:", len(chunks))
print("embedding shape:", chunk_embeddings.shape)

query = "what is deep learning ?"
query_embedding = model.encode([query])
print("query shape:", query_embedding.shape)

scores = util.cos_sim(query_embedding, chunk_embeddings)
# scored = list(zip(scores[0].tolist(), chunks))
# scored.sort(reverse=True)

# for score, chunk in scored[:2]:
#     print(round(score, 2), "->", chunk) 
print("score",scores)

top2 = scores.topk(2)
print(top2)
print("top 2 indices:", top2.indices)
print("top 2 scores:", top2.values)

for idx in top2.indices[0]:
    print(chunks[idx])

