import streamlit as st
from core.pipeline import run_pipeline

st.title("🧠 TruthLens AI")

query = st.text_input("Ask a question:")

if st.button("Submit"):
    result = run_pipeline(query)

    st.subheader("Answer")
    st.write(result["answer"])

    st.subheader("Confidence")
    st.progress(result["confidence"])

    st.subheader("Verification")
    st.write(result["verification"])

    st.subheader("Sources")
    st.write(result["sources"])
