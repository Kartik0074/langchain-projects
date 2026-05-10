from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

laod_dotenv()

model = ChatOpenAI(model='gpt-4o-mini')

while True:
    user_input = input('You: ')
     if user_input == 'exit':
        break
    result = model.invoke(user_input)
    print('Chatbot:', result.content)
    