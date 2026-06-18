from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv()

class ResearchOutput(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

#pick which llm to use (Anthropic is Claude, OpenAI is GPT), we're using chat because of the free API access, but you can use the non-chat versions if you want to
#llm = ChatAnthropic(model="claude-3-5-sonnet-20241022") #temperature=0.7)
llm2 = ChatOpenAI(model="gpt-4o-mini", temperature=0.7) 
parser = PydanticOutputParser(pydantic_object=ResearchOutput)

prompt = ChatPromptTemplate.from_messages(
  [
    ("system", 
     """
     You are a research assistant that gathers information on a 
     given topic and summarizes it in a clear and concise manner.
     Answer the user query and use necessary tools. 
     Wrap the output in this format and provide no other text
     """,
    ), 
    ("placeholder", "{chat_history}"), 
    ("human", "{query}"),
    ("placeholder", "{agent_scratchpad}"),
  ]
).partial(format_instructions=parser.get_format_instructions())

""" response = llm2.invoke("Is Fortnite still a good game?")
print(response)
"""