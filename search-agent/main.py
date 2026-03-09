from dotenv import load_dotenv
load_dotenv()
from typing import List
from pydantic import BaseModel, Field
from langchain.agents import create_agent 
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from tavily import TavilyClient
tavily=TavilyClient()


class Source(BaseModel):
    """Schema for source used by agent"""
    url:str = Field(description="url of the source")
    
class AgentResponse(BaseModel):
    """Schema for agent response with answer and sources"""

    answer:str = Field(description="The agent's answer to the query")
    sources:List[Source] = Field(default_factory=list, description="List of sources used to generate the answer")

@tool
def search(query:str) -> str:
    """
    Tool that searches over the internet and returns the result
    Args:
        query (str): The query to search for
    Returns:
        str: The result of the search
    """
    print(f"Searching for {query}")
    return tavily.search(query=query)
llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash")
tools =[search]
agent = create_agent(
    model=llm,
    tools=tools,
    response_format=AgentResponse
)
def main():
    print("Hello from search-agent!")
    result=agent.invoke({"messages":[HumanMessage(content="find java backend devevloper jobs in india for 1 year experienced proffesional and also include link to apply max 10 jobs ")]})
    print(result)


if __name__ == "__main__":
    main()
