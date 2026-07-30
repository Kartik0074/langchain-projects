# LangChain GenAI Learning Journey + YouTube Chatbot

Hey! This repo is my hands-on learning journey with Generative AI and LangChain. I started from zero and built up to a working RAG-based YouTube chatbot.

## What I Learned

**LLM and Chat Models**
Started with understanding the difference between LLMs and Chat models, how to call OpenAI API using LangChain and how to manage API keys securely using dotenv.

**Prompt Engineering**
Learned static vs dynamic prompts, built PromptTemplates and ChatPromptTemplates with variables, and understood why prompt templates are better than simple f-strings when working with chains.

**Messages**
Worked with SystemMessage, HumanMessage and AIMessage to build a terminal chatbot with chat history using MessagesPlaceholder.

**Chains (LCEL)**
Learned the pipe operator to connect prompts, models and parsers. Built simple, sequential and parallel chains using RunnableParallel, RunnablePassthrough and RunnableLambda.

**Structured Output and Output Parsers**
Used TypedDict and Pydantic to get structured JSON output from LLMs instead of plain text. Also learned StrOutputParser and JsonOutputParser to clean up chain outputs.

**RAG (Retrieval Augmented Generation)**
This was the most interesting part. Learned how to load documents, split them into chunks, convert them to embeddings, store in a vector database using FAISS, and retrieve relevant chunks to answer questions using semantic search.

## Project: YouTube Chatbot

Built a full RAG application where you paste any YouTube URL and chat with the video content.

**How it works:**
- Fetches the video transcript automatically
- Splits transcript into chunks
- Converts chunks to embeddings using OpenAI
- Stores in FAISS vector store
- User asks a question, it finds relevant parts and answers using GPT-4o-mini

**Tech Stack:**
- LangChain
- OpenAI GPT-4o-mini
- FAISS
- Streamlit
- Python

## How to Run
Add your OpenAI API key in a .env file:
Run the app:


### Stack

Python, LangChain, OpenAI, FAISS, Streamlit


Clone the repo and go to the Youtube_chatbot_RAG folder.

Install dependencies:
