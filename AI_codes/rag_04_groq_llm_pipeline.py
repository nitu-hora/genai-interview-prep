# Full Retrieval-Augmented Generation (RAG) flow:

# Load text — your data source
# Chunk — split into small pieces
# Embed — text → vectors
# Store — vectors into ChromaDB
# Query — embed the question → find top k similar chunks
# Prompt — chunks + question → one string
# Generate — send prompt to Large Language Model (LLM) → get answer

from sentence_transformers import SentenceTransformer
import chromadb
from  groq import Groq
from dotenv import load_dotenv
import os


load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

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

if collection.count() == 0:
    store_chunks(chunks, chunk_embeddings)
    print("stored", len(chunks), "chunks")


query = "what is deep learning?"
query_embeddings = model.encode(query)

result = collection.query(
    query_embeddings= [query_embeddings.tolist()],
    n_results= 2
    )

print(result["documents"])

top_chunks = result["documents"][0]

prompt = f"""Use these chunks to answer the question.

Chunks:
{top_chunks[0]}
{top_chunks[1]}

Question :{query}
"""

groq_client = Groq(api_key= api_key)
response = groq_client.chat.completions.create(
    model = "openai/gpt-oss-20b",
    messages = [{"role": "user", "content": prompt}]
)

print(response.choices[0].message.content)

