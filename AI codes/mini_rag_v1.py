text = """Machine learning is a way of making computers learn from data.
Deep learning uses neural networks with many layers.
Transformers are the architecture behind GPT and BERT.
Self-supervised learning creates labels from the data itself.
RAG combines retrieval with generation to asnwer questions."""

# def chunk_text(text, size = 100):
#     return [text[i:i+size] for i in range(0,len(text), size)]

def chunk_text(text):
    return [s.strip() for s in text.split('.') if s.strip() != ""]


# test = chunk_text(text)
# print(test)

def find_similar(query, chunks):
    stopwords = {"what", "is", "are", "the", "a", "an", "of", "in", "it"}
    query_words = set(query.lower().split()) - stopwords
    print('query words', query_words)
    scored = [(sum(1 for w in query_words if w in c.lower().split()), c) for c in chunks]
    for s in scored:
        print(s)
    return sorted(scored, reverse = True)[0][1]

chunks = chunk_text(text)
result = find_similar('what is deep learning ?', chunks)
print("retrived:", result)


# all the prints are for observation