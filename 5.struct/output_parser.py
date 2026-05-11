from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()   

llm = HuggingFaceEndpoint(
    repo-id="Tinayu/llama-2-7b-chat-hf",
    task="text-generation",

)

model = ChatHuggingFace(llm=llm)

template = PromptTemplate(
    template = 'write a detailed report on {topic}',
    input_variables=['topic']
)

template = PromptTemplate(
    template = 'write a 5 line summary report on {topic}',
    input_variables=['topic']
)



