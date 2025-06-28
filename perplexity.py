from together import Together
from dotenv import load_dotenv

load_dotenv()
client = Together()

def search_perplexity(query: str) -> str:
    """Search for real-time data using Perplexity AI"""
    
    response = client.chat.completions.create(
        model="perplexity-ai/r1-1776",
        messages=[{"role": "user", "content": f"Provide real-time data for: {query}"}]
    )
    return response.choices[0].message.content