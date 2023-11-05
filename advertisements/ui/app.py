import os
import streamlit as st
import requests
from dotenv import load_dotenv

with st.sidebar:
    st.markdown(
        "## How to use\n"
        "1. Choose data sources.\n"
        "2. Ask any questions related to advertisements of digital market.\n"
    )
    st.markdown("---")
    st.markdown("# About")
    st.markdown(
        "AI app to find real-time that gives quick insights into latest changes in digital marketingss' ads who are spending a lot of money (and thus taking more data-led decisions) "
        "It uses Pathway’s [LLM App features](https://github.com/pathwaycom/llm-app) "
        "to build real-time LLM(Large Language Model)-enabled data pipeline in Python and join data from multiple input sources\n"

    )
##################st.markdown("[View the source code on GitHub](https://github.com/Boburmirzo/chatgpt-api-python-sales)")

# Load environment variables
load_dotenv()
api_host = os.environ.get("HOST", "0.0.0.0")
api_port = int(os.environ.get("PORT", 8080))

# Streamlit UI elements
st.title("AdsGPT: Getting quick insights into digital marketing ads")

question = st.text_input(
    "Ask a Question",
    placeholder="Give me a list of new ad published by Amazon.",
)

if question:
    url = f'http://{api_host}:{api_port}/'
    data = {"query": question}

    response = requests.post(url, json=data)

    if response.status_code == 200:
        st.write("### Answer")
        st.write(response.json())
    else:
        st.error(f"Failed to send data to the Pathway API. Status code: {response.status_code}")