import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import spacy
import pytextrank

# Load Fine-Tuned Model & Tokenizer
@st.cache_resource
def load_abstractive_model():
    tokenizer = AutoTokenizer.from_pretrained("amusEcode/summarizer-tokenizer")
    model = AutoModelForSeq2SeqLM.from_pretrained("amusEcode/summarizer_model")
    return tokenizer, model

tokenizer, model = load_abstractive_model()

# Load spaCy & PyTextRank
@st.cache_resource
def load_textrank():
    nlp = spacy.load("en_core_web_sm")
    nlp.add_pipe("textrank")
    return nlp

nlp = load_textrank()

# App Config
st.set_page_config(
    page_title="Text Summarizer",
    page_icon="📝",
    layout="wide"
)

st.title("🧠 Text Summarizer App")
st.markdown(
    "Choose between **Abstractive (BART)** and **Extractive (PyTextRank)** summarization."
)

# User Inputs
choice = st.selectbox("Select Summarization Type", ["Abstractive (BART)", "Extractive (PyTextRank)"])
text = st.text_area("Enter the text you want to summarize:", height=250)

# Abstractive sliders
max_len = st.slider("Maximum summary length (Abstractive)", 50, 250, 120)
min_len = st.slider("Minimum summary length (Abstractive)", 20, 100, 40)

# Extractive slider
num_sentences = st.slider("Number of sentences for extractive summary", 1, 10, 3)

# Summarization
if st.button("Generate Summary"):
    if not text.strip():
        st.warning("Please enter some text to summarize.")
    else:
        with st.spinner("Generating summary... ⏳"):
            if "Abstractive" in choice:
                # Tokenize input
                inputs = tokenizer(
                    [text],
                    max_length=512,
                    truncation=True,
                    padding=True,
                    return_tensors="pt"
                )

                # Generate summary
                summary_ids = model.generate(
                    inputs["input_ids"],
                    max_length=max_len,
                    min_length=min_len,
                    length_penalty=2.0,
                    num_beams=4
                )
                summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

            else:
                try:
                    doc = nlp(text)
                    extractive_summary_sentences = [
                        sent.text for sent in doc._.textrank.summary(limit_sentences=num_sentences)
                    ]
                    summary = " ".join(extractive_summary_sentences)
                    if not summary.strip():
                        summary = "Extractive summary too short or not available."
                except Exception as e:
                    summary = f"Error generating extractive summary: {e}"

        # Display summary
        st.subheader("📝 Summary")
        st.write(summary)
