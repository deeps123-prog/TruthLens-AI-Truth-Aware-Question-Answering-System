from openai import OpenAI
from app.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

EMBEDDING_MODEL = "text-embedding-3-small"


def get_embedding(text: str) -> list:
    """
    Generate embedding for a single text input.
    """
    if not text:
        return []

    response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=text
    )
    return response.data[0].embedding


def get_embeddings_batch(texts: list) -> list:
    """
    Generate embeddings for a batch of texts.
    """
    if not texts:
        return []

    response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=texts
    )
    return [item.embedding for item in response.data]


# --- Optional Utility Functions (VERY useful later) ---

def cosine_similarity(vec1: list, vec2: list) -> float:
    """
    Compute cosine similarity between two vectors.
    """
    if not vec1 or not vec2:
        return 0.0

    dot_product = sum(a * b for a, b in zip(vec1, vec2))
    norm1 = sum(a * a for a in vec1) ** 0.5
    norm2 = sum(b * b for b in vec2) ** 0.5

    if norm1 == 0 or norm2 == 0:
        return 0.0

    return dot_product / (norm1 * norm2)


def find_most_similar(query_embedding: list, doc_embeddings: list) -> int:
    """
    Return index of most similar document.
    """
    similarities = [
        cosine_similarity(query_embedding, emb)
        for emb in doc_embeddings
    ]

    if not similarities:
        return -1

    return similarities.index(max(similarities))
