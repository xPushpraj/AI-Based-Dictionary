## building streamlit application of dictionary using langchain

import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
import os

# --------------------------
# --- Sidebar Setup
# --------------------------
with st.sidebar:
    st.subheader("🔑 API Configuration")

    # Input fields for user-provided API key and model
    api_key = st.text_input("Enter your OpenRouter API Key:", type="password")
    model_name = st.text_input("Enter Model Name:", value="google/gemini-2.5-flash-preview-09-2025")

    temperature = st.slider("Creativity (temperature)", 0.0, 1.0, 0.5)
    max_tokens = st.number_input("Max Tokens", min_value=50, max_value=2000, value=100, step=50)

# --------------------------
# --- Validate API Setup
# --------------------------
if not api_key:
    st.warning("⚠️ Please enter your API Key in the sidebar.")
    st.stop()

# Set environment for LangChain dynamically
os.environ["OPENAI_API_KEY"] = api_key
os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/api/v1"

# --------------------------
# --- Initialize LLM
# --------------------------
try:
    llm = ChatOpenAI(
        model=model_name,
        temperature=temperature,
        max_tokens=max_tokens
    )
    st.success(f"✅ Using model: {model_name}")
except Exception as e:
    st.error(f"❌ Failed to initialize model: {str(e)}")
    st.stop()

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
            with st.spinner("Generating definition..."):
                llm = ChatOpenAI(
                    model="x-ai/grok-4-fast:free", 
                    temperature=0.85,
                    max_tokens=100
                )
                prompt_template = ChatPromptTemplate.from_messages([
                    ("system", "Define the word in single line or just tell the simplest meaning of the word , antonym and synonym all of are in different line:  {word}"),
                    ("user", "{word}")
                ])
                story_prompt = prompt_template.format(
                    word=word
                )
                response = llm.invoke(story_prompt)
                st.write(response.content)

