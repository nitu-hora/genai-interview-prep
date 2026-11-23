# Full Retrieval-Augmented Generation (RAG) flow - v6:

# Load text — your data source
# Chunk — split into small pieces (NLTK, size=500, overlap=50)
# Embed — text → vectors (SentenceTransformer)
# Store — vectors into ChromaDB (once, if empty)
# Expand — LLM generates 3 sub-queries from original question
# Query — run all 3 sub-queries against ChromaDB
# Merge + Dedup — combine 9 chunks, remove repeats
# Prompt — unique chunks + question → one string
# Generate — send prompt to LLM → get answer

from sentence_transformers import SentenceTransformer
import chromadb
from  groq import Groq
from dotenv import load_dotenv
import os
import nltk 
nltk.download("punkt_tab")
from nltk.tokenize import sent_tokenize


load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

text = """Machine learning is a way of making computers learn from data.
Deep learning uses neural networks with many layers.
Transformers are the architecture behind GPT and BERT.
Self-supervised learning creates labels from the data itself.
RAG combines retrieval with generation to asnwer questions."""

def chunk_text(text, size = 500, overlap = 50):
    sentences = sent_tokenize(text)
    chunks = []
    current_chunk = ""

    for sentence in sentences:
        if len(current_chunk) + len(sentence) <= size:
            current_chunk += " " + sentence
        else:
            chunks.append(current_chunk.strip())
            current_chunk = current_chunk[-50:]+ " " + sentence

    if current_chunk.strip():
        chunks.append(current_chunk.strip())

    return chunks

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


question = "what is deep learning?"

groq_client = Groq(api_key= api_key)

def generate_subqueries(question,groq_client):
    prompt = f" Give me 3 queries for the {question}, one per line"
    response = groq_client.chat.completions.create(
        model = "openai/gpt-oss-20b",
        messages = [{"role": "user", "content": prompt}]
        )
    text = response.choices[0].message.content
    return text.strip().split("\n")

def run_all_queries(subqueries, collection, model):
    all_chunks = []
    for query in subqueries:
        query_embeddings = model.encode(query)
        result = collection.query(
            query_embeddings = [query_embeddings.tolist()],
            n_results = 3
        )
        chunks = result["documents"][0]
        all_chunks.extend(chunks)
    return all_chunks

def merge_and_dedup(all_chunks):
    return list(set(all_chunks))

subqueries = generate_subqueries(question, groq_client)
all_chunks = run_all_queries(subqueries, collection, model)
top_chunks = merge_and_dedup(all_chunks)

prompt = f"""Use these chunks to answer the question.

Chunks:
{top_chunks[0]}
{top_chunks[1]}
{top_chunks[2]}

Question :{question}
"""


response = groq_client.chat.completions.create(
    model = "openai/gpt-oss-20b",
    messages = [{"role": "user", "content": prompt}]
)

print(response.choices[0].message.content)


# print(chunk_text(text, size=100, overlap=20))