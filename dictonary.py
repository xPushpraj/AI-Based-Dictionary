## building streamlit application of dictionary using langchain

import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
import os

# --------------------------
# --- API Setup (OpenRouter)
# --------------------------
os.environ["OPENAI_API_KEY"] = "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"   # 🔑 Replace with your key
os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/api/v1"

llm = ChatOpenAI(
    model="google/gemini-2.5-flash-preview-09-2025", 
    temperature=0.5,
    max_tokens=200
)

# --------------------------
# Page Config
# --------------------------
st.set_page_config(page_title="Dictionary", page_icon="📖", layout="centered")

st.title("Dictionary")

# --- Main Input Form ---
st.subheader("Word to Define")
word = st.text_input("Enter a word:")

if st.button("Define"):
    if word:
        st.write(f"Definition of {word} is :")

##creating container for defination section  
with st.container():
    with st.status("Generating definition..."):
        llm = ChatOpenAI(
            model="x-ai/grok-4-fast:free", 
            temperature=0.85,
            max_tokens=800
        )
        prompt_template = ChatPromptTemplate.from_messages([
            ("system", "Define the word in single line or just tell the simplest meaning of the word , antonym and synonym all of are in different line:  {word}"),
            ("user", "Define the word in single line or just tell the simplest meaning of the word , antonym and synonym all of are in different line: {word}")
        ])
        story_prompt = prompt_template.format(
            word=word
        )
        response = llm.invoke(story_prompt)
        st.write(response.content)

