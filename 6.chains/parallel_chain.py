from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableParallel
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model1 = ChatOpenAI(model='gpt-4o-mini')
model2 = HuggingFaceEndpoint(model='google/flan-t5-xxl')

prompt1 =  PromptTemplate(
    template='write a detailed report on {topic}',
    input_variables=['topic']
)

pormpt2 = PromptTemplate(
    template='write a 5 line summary on {text}',    
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template='merege the providded notes and quiz into a single document \n notes -> {notes} \n quiz -> {quiz}', and input_variables=['notes', 'quiz']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz': pormpt2 | model2 | parser

})

merge_chain = prompt3 | model1 | parser

chain = parallel_chain | merge_chain



result =chain.invoke({'topic': 'football'})

print(result)
