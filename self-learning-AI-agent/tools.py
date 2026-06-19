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