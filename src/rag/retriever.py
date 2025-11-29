import chromadb
client = chromadb.Client()
collection = client.get_or_create_collection("kb")

def store_chunks(chunks, vectors):
    for i,c in enumerate(chunks):
        collection.add(documents=[c], embeddings=[vectors[i]], ids=[str(i)])

def retrieve_context(query):
    res=collection.query(query_texts=[query], n_results=3)
    return "\n".join(res['documents'][0]) if res['documents'] else ""
