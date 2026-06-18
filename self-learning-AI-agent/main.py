from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

load_dotenv()

#pick which llm to use (Anthropic is Claude, OpenAI is GPT)

#llm = ChatAnthropic(model="claude-3-5-sonnet-20241022") #temperature=0.7)
llm2 = ChatOpenAI(model="gpt-4o-mini", temperature=0.7) 
response = llm2.invoke("What is the meaning of life?")
print(response)