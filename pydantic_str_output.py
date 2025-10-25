from langchain_google_genai import ChatGoogleGenerativeAI
import os 
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Optional,Literal
from pydantic import BaseModel,Field

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

model = ChatGoogleGenerativeAI( api_key=api_key, model="gemini-2.5-flash",)

# Schema
class Review(BaseModel):

    key_themes:list[str]=Field(description="write down all the key themes discussed in the review")
    summary:str=Field(description="Brief summary of the review")
    sentiment:Literal["positive","negative"] = Field(description="one word for negative,positive or neutral")
    pros:Optional[list[str]]=Field(default=None,description="List down pros of product from review ")
    cons:Optional[list[str]]=Field(default=None,description="List down cons of product from review ")
    name:Optional[str]=Field(default=None,description="name of the reviewer")

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it's an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I'm gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

    The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

    However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung's One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

    Pros:
    Insanely powerful processor (great for gaming and productivity)
    Stunning 200MP camera with incredible zoom capabilities
    Long battery life with fast charging
    S-Pen support is unique and useful

    Cons:
    Bulky and heavy—not great for one-handed use
    Bloatware still exists in One UI
    Expensive compared to competitors""")

print(result.name)