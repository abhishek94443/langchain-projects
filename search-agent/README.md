# Search Agent

This project is a Langchain-based search agent. Below are the setup steps and an explanation of the commands used to initialize it.

## Setup Steps

### 1. Initialize the Project
```bash
uv init
```
**Explanation:** 
This command initializes a new Python project using `uv` (a fast Python package installer and resolver). It sets up the basic project structure, including the `pyproject.toml` file for managing metadata and dependencies, as well as a virtual environment and a boilerplate `main.py` file.

### 2. Install Langchain and Integrations
```bash
uv add langchain langchain-google-genai langchain-tavily
```
*(Note: If you ran `uv langchain...`, the correct command to add dependencies is `uv add ...`)*

**Explanation:**
This command adds three essential packages to the project's dependencies and installs them:
- **`langchain`**: The core framework for developing applications powered by large language models (LLMs).
- **`langchain-google-genai`**: The integration package that allows Langchain to use Google's Gemini AI models.
- **`langchain-tavily`**: The integration package for Tavily, a search engine designed specifically for AI agents to perform accurate and fast web searches.

### 3. Install Utilities and Formatting Tools
```bash
uv add python-dotenv black isort
```

**Explanation:**
This command installs three helpful development and configuration tools:
- **`python-dotenv`**: Used to load environment variables (such as `GOOGLE_API_KEY` and `TAVILY_API_KEY`) from a local `.env` file into the application. This ensures that sensitive API keys are kept secure.
- **`black`**: An uncompromising code formatter for Python. It automatically formats your Python code to comply with a strict, consistent style guide, saving you from manually formatting code.
- **`isort`**: A Python utility that automatically sorts and groups your import statements (e.g., standard library imports, third-party imports, and local application imports) alphabetically and by type, keeping your files clean and organized.

### 4. Install Tavily Python SDK
```bash
uv add tavily-python
```

**Explanation:**
This command installs the official Tavily Python SDK package. Even though we installed `langchain-tavily` earlier (which provides Langchain's specific wrapper for Tavily), our `main.py` explicitly tries to import the base `TavilyClient`, which requires the raw `tavily-python` dependency.

### 5. Add Structured Outputs with Pydantic
In `main.py`, we added Pydantic schemas to strictly enforce the shape of the data the AI agent returns.

**Explanation:**
By defining Python classes that inherit from `BaseModel`, we can tell Langchain exactly how we want the AI's response to be formatted.
- `Source`: A model that expects a single `url` string.
- `AgentResponse`: A model that expects an `answer` string and a list of `sources` (using the `Source` model).

When we pass `response_format=AgentResponse` into `create_agent()`, the language model ensures its final output matches this exact JSON structure! This is perfect for when you need to use the AI's output programmatically instead of just printing raw text.
