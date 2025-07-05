from langchain_openai import ChatOpenAI
import os
import streamlit as st


def get_openai_model():
    # Get API key from environment variables
    api_key = st.secrets("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OpenAI API key not found in environment variables")
        
    llm = ChatOpenAI(
        api_key=api_key,
        model="gpt-4o-mini",
        temperature=0.7
    )
    return llm
