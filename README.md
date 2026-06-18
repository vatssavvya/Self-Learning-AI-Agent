# AI Research Agent

A Python-based AI agent that acts as a research assistant. It takes a user query, searches the web and Wikipedia for information, structures the findings into specific categories, and writes the output to a local text file.

## Features
- **Structured Data:** Uses Pydantic to ensure outputs contain specific fields (Topic, Summary, Sources, Tools Used).
- **Web Tools:** Integrated with Wikipedia and DuckDuckGo for real-time information retrieval.
- **File Management:** Includes a custom tool that writes data to local text files with a timestamp.
- **LLM Compatibility:** Supports both OpenAI and Anthropic API models.

## Project Structure
- `main.py`: Contains the main prompt templates, agent executor initialization, and logic.
- `tools.py`: Contains definitions for the search utilities and the file-saving tool.
- `.env`: Stores required API keys.
- `requirements.txt`: List of dependencies.

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-folder>
