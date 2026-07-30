import streamlit as st
from dotenv import load_dotenv
from rag import load_youtube_transcript, build_vectorstore, get_answer

load_dotenv()

st.set_page_config(page_title="YouTube Chatbot", page_icon="🎬", layout="centered")

st.markdown("""
    <style>
        .main { background-color: #0f0f0f; }
        .block-container { padding-top: 2rem; }
        h1 { color: #ff0000; font-size: 2.2rem; }
        .stTextInput input, .stTextArea textarea {
            background-color: #1a1a1a;
            color: #ffffff;
            border: 1px solid #333;
            border-radius: 8px;
        }
        .stButton button {
            background-color: #ff0000;
            color: white;
            border-radius: 8px;
            font-weight: bold;
            width: 100%;
        }
        .stButton button:hover { background-color: #cc0000; }
        .answer-box {
            background-color: #1a1a1a;
            border-left: 4px solid #ff0000;
            padding: 1rem 1.2rem;
            border-radius: 8px;
            color: #f0f0f0;
            margin-top: 1rem;
        }
        .chat-human {
            background-color: #1e1e1e;
            border-radius: 8px;
            padding: 0.6rem 1rem;
            margin: 0.3rem 0;
            color: #cccccc;
        }
        .chat-bot {
            background-color: #2a1a1a;
            border-left: 3px solid #ff0000;
            border-radius: 8px;
            padding: 0.6rem 1rem;
            margin: 0.3rem 0;
            color: #f0f0f0;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("# 🎬 YouTube Chatbot")
st.markdown("Paste a YouTube URL and ask anything about the video.")

st.divider()

url = st.text_input("🔗 YouTube URL", placeholder="https://www.youtube.com/watch?v=...")

if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "loaded_url" not in st.session_state:
    st.session_state.loaded_url = ""

if st.button("Load Video"):
    if not url.strip():
        st.warning("Please enter a YouTube URL.")
    else:
        with st.spinner("Fetching transcript and building knowledge base..."):
            try:
                docs = load_youtube_transcript(url)
                st.session_state.vectorstore = build_vectorstore(docs)
                st.session_state.chat_history = []
                st.session_state.loaded_url = url
                st.success("✅ Video loaded! Ask your questions below.")
            except Exception as e:
                st.error(f"❌ Error loading video: {str(e)}")

if st.session_state.vectorstore:
    st.divider()
    st.markdown("### 💬 Ask anything about the video")

    question = st.text_input("Your question", placeholder="Summarize the video / What is explained at the start?")

    if st.button("Get Answer"):
        if not question.strip():
            st.warning("Please enter a question.")
        else:
            with st.spinner("Thinking..."):
                try:
                    answer = get_answer(st.session_state.vectorstore, question)
                    st.session_state.chat_history.append({
                        "question": question,
                        "answer": answer
                    })
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")

    if st.session_state.chat_history:
        st.divider()
        st.markdown("### 🗂 Chat History")
        for chat in reversed(st.session_state.chat_history):
            st.markdown(f'<div class="chat-human">🙋 {chat["question"]}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="chat-bot">🤖 {chat["answer"]}</div>', unsafe_allow_html=True)

        if st.button("🗑 Clear Chat"):
            st.session_state.chat_history = []
            st.rerun()