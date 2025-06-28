from langchain.tools import tool
from perplexity import fetch_realtime_data_perplexity

@tool(description="Search using Perplexity and return the result as a string.")
def perplexity_search_tool(query: str):
    return fetch_realtime_data_perplexity(query)