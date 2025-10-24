from langchain_google_genai import ChatGoogleGenerativeAI
import os 
from dotenv import load_dotenv
from typing import TypedDict,Annotated

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

model = ChatGoogleGenerativeAI( api_key=api_key, model="gemini-2.5-flash",)

# Schema
class Review(TypedDict):
    summary: Annotated[str,"Brief summary of the review"]
    sentiment: Annotated[str,"one word for negative,positive or neutral"]

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""The hardware is great, but the software feels bloated. There are too many pre-installed apps that I can't remove. Also, the UI looks outdated compared to other brands. Hoping for a software update to fix this.""")

print(result)