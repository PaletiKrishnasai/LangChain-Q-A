# QandA Chatbot - attempt 1
from langchain.llms import OpenAI

# from dotenv import load_dotenv
import os

# take environment variables from .env
# load_dotenv()

import streamlit as st

# load OpenAI model and get a response


def get_openai_response(question):
    llm = OpenAI(
        openai_api_key=os.getenv("OPEN_API_KEY"),
        model_name="text-davinci-003",
        temperature=0.6,
    )
    response = llm(question)
    return response
    # modify with chain and other stuff


## streamlit app

st.set_page_config(page_title="QandA Demo")
st.header("Langchain Application")

input = st.text_input("Input: ", key=input)
response = get_openai_response(input)


submit = st.button("Generate")
if submit:
    st.subheader("The response is")
    st.write(response)
