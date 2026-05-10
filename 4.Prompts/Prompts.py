from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

model = ChatOpenAI(model='gpt-4o-mini')

st.header('Research Tool')

paper_input = st.selectbox("Select a research paper:", ["Paper 1", "Paper 2", "Paper 3"])

style_input = st.selectbox("Select a writing style:", ["Academic", "Informal", "Technical"])

length_input = st.slider("Select the desired length of the answer:", 100, 1000, 500)

user_input = st.text_input("Enter your research question:")

if st.button('Get Answer'):
    result = model.invoke(user_input)
    st.write(result.content)