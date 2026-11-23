from sentence_transformers import SentenceTransformer
import chromadb

text = """Machine learning is a way of making computers learn from data.
Deep learning uses neural networks with many layers.
Transformers are the architecture behind GPT and BERT.
Self-supervised learning creates labels from the data itself.
RAG combines retrieval with generation to asnwer questions."""

def chunk_text(text):
    return [t.strip() for t in text.split('.') if t.strip() != ""]

model = SentenceTransformer("all-MiniLM-L6-v2")
print("model loaded")

client = chromadb.PersistentClient(path = "./chroma_db")
collection = client.get_or_create_collection(name = "text_collection")

chunks = chunk_text(text)
chunk_embeddings = model.encode(chunks)

def store_chunks(chunks, chunk_embeddings):
    collection.add(
        documents=chunks,
        embeddings=chunk_embeddings.tolist(),
        ids=[f"chunk_{i}" for i in range(len(chunks))]
        )

store_chunks(chunks,chunk_embeddings)
print("stored", len(chunks), "chunks")

query = "what is deep learning?"
query_embeddings = model.encode(query)

result = collection.query(
    query_embeddings= [query_embeddings.tolist()],
    n_results= 2
    )

print(result["documents"])

