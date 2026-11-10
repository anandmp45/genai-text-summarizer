import os
import streamlit as st
from google import genai
from google.genai import types

st.set_page_config(page_title="GenAI Text Summarizer", page_icon="🧠", layout="centered")

st.title("🧠 GenAI Text Summarizer")
st.caption("Turn long text into clear, useful summaries using Generative AI.")

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    st.warning("Add your Gemini API key as the GEMINI_API_KEY environment variable to enable AI summarization.")

text = st.text_area(
    "Paste your text here",
    height=260,
    placeholder="Paste an article, class notes, or any text you want summarized..."
)
style = st.selectbox("Summary style", ["Short bullet points", "Simple paragraph", "Study notes"])
length = st.select_slider("Summary length", options=["Very short", "Short", "Medium", "Detailed"], value="Medium")

if st.button("Generate summary", type="primary", use_container_width=True):
    if not text.strip():
        st.error("Please paste some text first.")
    elif not api_key:
        st.error("AI is not connected yet. Set GEMINI_API_KEY and restart the app.")
    else:
        try:
            client = genai.Client(api_key=api_key)
            prompt = f"""
You are a careful summarization assistant.
Summarize the text below.
Format: {style}
Length: {length}
Keep important facts and names accurate. Do not invent details.
If the source text is unclear, say so.

SOURCE TEXT:
{text}
"""
            with st.spinner("Generating your summary..."):
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt,
                    config=types.GenerateContentConfig(temperature=0.2)
                )
            st.subheader("Your summary")
            st.write(response.text or "The AI returned an empty response.")
            st.download_button(
                "Download summary",
                data=response.text or "",
                file_name="summary.txt",
                mime="text/plain",
                use_container_width=True
            )
        except Exception as exc:
            st.error("The request could not be completed. Check your API key, internet connection, and model availability.")
            st.caption(f"Technical detail: {exc}")

with st.expander("How this project works"):
    st.markdown(
        "1. The user enters text and chooses a summary format.\\n"
        "2. The Streamlit app sends a prompt and the text to the Gemini API.\\n"
        "3. Gemini generates a summary.\\n"
        "4. The app displays the result and lets the user download it."
    )

st.caption("Educational demo. Review AI-generated summaries for accuracy before relying on them.")
