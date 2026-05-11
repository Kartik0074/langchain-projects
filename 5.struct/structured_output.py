from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

class Review(TypedDict):
    summary: str
    sentiment: str

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("The iPhone 16 features the A18 chip with impressive performance gains. The camera system has been upgraded with a new Camera Control button for easier shooting. Battery life is noticeably better than the 15. The design is similar to iPhone 15 but feels more premium in hand. Overall a solid upgrade if you're coming from iPhone 13 or older.")

print("Result: ")
print(result)
