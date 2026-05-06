from core.pipeline import run_pipeline

if __name__ == "__main__":
    query = input("Enter your query: ")
    result = run_pipeline(query)

    print("\nAnswer:\n", result["answer"])
    print("\nConfidence:", result["confidence"])
