from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor

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
     Wrap the output in this format and provide no other text\n{format_instructions}
     """,
    ), 
    ("placeholder", "{chat_history}"), 
    ("human", "{query}"),
    ("placeholder", "{agent_scratchpad}"),
  ]
).partial(format_instructions=parser.get_format_instructions())

agent = create_tool_calling_agent(
    llm=llm2, 
    prompt=prompt, 
    tools=[]
)

agent_executor = AgentExecutor(
    agent=agent, 
    tools=[], 
    verbose = True
)
raw_response = agent_executor.invoke({"query": "Fortnite or Roblox, which is better?", "name": "Savya"})
#print(raw_response)

try:
    structured_response = parser.parse(raw_response.get("output")[0]["text"])
except Exception as e:
    print(f"Error parsing structured response: {e}", "Raw Response: ", raw_response)


