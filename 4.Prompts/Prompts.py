from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

model = ChatOpenAI(model='gpt-4o-mini')

st.header('Research Tool')

user_input = st.text_input("Enter your research question:")

if st.button('Get Answer'):
    result = model.invoke(user_input)
    st.write(result.content)