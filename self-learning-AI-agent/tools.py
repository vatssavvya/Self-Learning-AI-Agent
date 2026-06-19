from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun, GoogleSearchRun, PythonREPLTool, TerminalTool, ShellTool
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool
from datetime import datetime

search = DuckDuckGoSearchRun()
search_tool = Tool(
    name="DuckDuckGo_Search",
    func=search.run,
    description="useful for when you need to search the web"
)

api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max = 100) #if we want to return n number of results, change the number to n, and doc content increases the rate limit usage
wikipedia_tool = WikipediaQueryRun(api_wrapper=api_wrapper)