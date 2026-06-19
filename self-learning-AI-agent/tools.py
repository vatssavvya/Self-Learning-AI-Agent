from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun, GoogleSearchRun, PythonREPLTool, TerminalTool, ShellTool
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool
from datetime import datetime

#custom function, you can create your own tool with a similar format
def save_to_txt(data: str, filename: str = None) -> str:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    formatted_text = f"{timestamp}: {data}\n"

    with open(filename, "a", encoding="utf-8") as file:
        file.write(formatted_text)

    return f"Data saved to {filename}"

save_tool = Tool(
    name="Save_Text_To_File",
    func=save_to_txt,
    description="useful for when you want to save some information to a text file, provide the data and filename as arguments"
)

search = DuckDuckGoSearchRun()
search_tool = Tool(
    name="DuckDuckGo_Search",
    func=search.run,
    description="useful for when you need to search the web"
)

api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max = 100) #if we want to return n number of results, change the number to n, and doc content increases the rate limit usage
wikipedia_tool = WikipediaQueryRun(api_wrapper=api_wrapper)