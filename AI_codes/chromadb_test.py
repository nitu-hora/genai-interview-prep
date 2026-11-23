# Creating the database from scratch
import chromadb

client = chromadb.PersistentClient(path="any_folder_name")
collection = client.get_or_create_collection(name="any_collection_name")

collection.add(
    ids=["lec1::0", "lec1::1"],
    documents=["LoRA adds small matrices to a frozen model...", "Attention lets each word look at others..."],
    metadatas=[{"lecture": "lec1"}, {"lecture": "lec1"}],
)

result = collection.query(query_texts=["what is lora"], n_results=2)