# Q&A Chatbot

from langchain.llms import OpenAI
from dotenv import load_dotenv
import streamlit as st
import os
load_dotenv()

# OpenAI_key = 
## Function to load Open AI model and get responses
# print(OpenAI_key)
def get_openai_response(question):
    llm=OpenAI(openai_api_key=os.getenv('OPENAI_API_KEY') ,model_name = "gpt-3.5-turbo-instruct", temperature=0.7)
    response=llm(question)
    return response


# Initialize streamlit
    
st.set_page_config(page_title="Q&A LLM App")
st.header("Langchain APP")

input= st.text_input("Input: ", key="input")
# get_openai_response(input)
response = get_openai_response(input)
submit= st.button("Ask the question")

if submit:
    

    st.subheader("The Response is")
    st.write(response)