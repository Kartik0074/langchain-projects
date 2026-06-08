from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel , RunnablePassthrough, RunnableSequence
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


prompt1 =  PromptTemplate(
    template='write a joke on {topic}',
    input_variables=['topic']
)

model1 = ChatOpenAI(model='gpt-4o-mini')    

parser = StrOutputParser()

prompt2 = PromptTemplate(
    template='explain the joke {topic}',
    input_variables=['topic']
)
joke_gen_chain = RunnableSequence(prompt1 | model1 | parser)

parallel_chain = RunnableParallel({
    'joke' : RunnablePassthrough(),
    'explanation' : RunnableSequence(prompt2 | model1 | parser)
})


final_chain = RunnableSequence(joke_gen_chain , explain_chain)
print(final_chain.invoke({'topic': 'football'}))
