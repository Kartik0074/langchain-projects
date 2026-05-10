from langchain_core.messages import SystemMessages, HumanMessages, AIMessage
from langchain_openai import ChatOpenAI

load_dotenv()
model = ChatOpenAI(model='gpt-4o-mini')

messages = [
    SystemMessages(content="You are a helpful assistant."),
    HumanMessages(content="What is the capital of France?"),
]

model.invoke(messages)
