from core.retriever import retrieve
from core.generator import generate_answer
from core.verifier import verify_answer
from core.confidence import compute_confidence

def run_pipeline(query):
    docs = retrieve(query)
    context = " ".join([d["content"] for d in docs])

    answer = generate_answer(query, context)
    verification = verify_answer(query, answer, context)

    confidence = compute_confidence(answer, verification)

    return {
        "answer": answer,
        "confidence": confidence,
        "verification": verification,
        "sources": docs
    }
