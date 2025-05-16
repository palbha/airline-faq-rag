import pandas as pd
import openai
df=pd.read_csv("data/faq_data.csv")
print(df)

from openai import OpenAI
#Feel free to use chatgpt or other models - Google offere free gemini api hence I have used this


import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np


# Optional: chunk answers into smaller pieces (e.g. 200 tokens) for better retrieval
def chunk_text(text, max_tokens=200):
    words = text.split()
    for i in range(0, len(words), max_tokens):
        yield " ".join(words[i:i+max_tokens])

chunks = []
metadata = []
for idx, row in df.iterrows():
    for c in chunk_text(row['answer']):
        chunks.append(c)
        metadata.append({
            "topic": row['topic'],
            "question": row['question'],
            "answer_chunk": c
        })


from sentence_transformers import SentenceTransformer
import numpy as np
#I am using the huggingface model to generate embeddings , If the data was large once can try & explore other embeddings
embedder = SentenceTransformer('all-MiniLM-L6-v2')

# Embed chunks
chunk_vectors = embedder.encode(chunks, convert_to_numpy=True)

# Build FAISS index as before
import faiss

dimension = chunk_vectors.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(chunk_vectors)

# For query embedding function
def embed_query(query):
    return embedder.encode([query], convert_to_numpy=True)[0]
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(df['question'])
def retrieve_similar_answer_chunks(query, k=5):
    q_vec = embed_query(query)
    D, I = index.search(np.array([q_vec]).astype('float32'), k)
    return [metadata[i] for i in I[0]]

def retrieve_similar_questions(query, k=5):
    q_tfidf = tfidf_vectorizer.transform([query])
    scores = (tfidf_matrix @ q_tfidf.T).toarray()
    topk_idx = scores[:,0].argsort()[-k:][::-1]
    return df.iloc[topk_idx][['topic', 'question', 'answer']].to_dict(orient='records')
def hybrid_retrieve(query, k=5):
    answer_chunks = retrieve_similar_answer_chunks(query, k)
    question_hits = retrieve_similar_questions(query, k)
    combined_contexts = answer_chunks + question_hits

    # Deduplicate if needed
    seen = set()
    filtered = []
    for c in combined_contexts:
        key = (c.get('topic'), c.get('question'))
        if key not in seen:
            filtered.append(c)
            seen.add(key)
    return filtered

def generate_answer(query,model_choice,api_key):
    contexts = hybrid_retrieve(query, k=5)
    context_text = "\n\n".join([f"Q: {c['question']}\nA: {c.get('answer') or c.get('answer_chunk')}" for c in contexts])

    messages = [
        {
            "role": "system",
            "content": (
                "You are an expert airline assistant answering user queries based on provided context."
                " Use the context to generate a helpful, factual, self-contained answer."
                "If the context doesn't help & you are unable to answer - Please reply to the user to reach out to our customer service call center at 1 800 800 000 or email us at customercare@airlinex.com"
                "If the user is asking some random question not related to be asked to an airline assistant reply - I don't understand your question can you please rephrase"
            )
        },
        {
            "role": "user",
            "content": f"Context:\n{context_text}\n\nQuestion: {query}\nAnswer:"
        }
    ]
    openai = OpenAI(
       base_url="https://generativelanguage.googleapis.com/v1beta/",
      api_key=api_key,
    )

    response = openai.chat.completions.create(
        model="gemini-1.5-flash",
        messages=messages,
        temperature=0.7,
        max_tokens=700,
    )
    return response.choices[0].message.content
