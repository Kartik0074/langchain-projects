from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


prompt1 =  PromptTemplate(
    template='write a tweeter post on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='write a facebook post on {topic}',
    input_variables=['topic']
)

model1 = ChatOpenAI(model='gpt-4o-mini')
model2 = ChatOpenAI(model='gpt-4o-mini')    

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'tweeter': prompt1 | model1 | parser,
    'facebook': prompt2 | model2 | parser

})

result =parallel_chain.invoke({'topic': 'football'})
print(result)

parallel_chain.get_graph().print_ascii()