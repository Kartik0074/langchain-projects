from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

promt1 = PromptTemplate(
    template='write a detailed report on {topic}', 
    input_variables=['topic']
)

promt2 = PromptTemplate(
    template='write a 5 line summary on {text}',
    input_variables=['text']
)

model = ChatOpenAI(model='gpt-4o-mini')

parser = StrOutputParser()

chain = promt1 | model | promt2 | model | parser

result = chain.invoke({'topic': 'fotball'})

print(result)

