from together import Together
from dotenv import load_dotenv

load_dotenv()

client = Together()

def fetch_realtime_data_perplexity(query: str):

    prompt = f"User question : {query}, please provide real time data regarding user question."

    response = client.chat.completions.create(
        model="perplexity-ai/r1-1776",
        messages=[
        {
            "role": "user",
            "content": prompt
        }
        ]
    )
    return response.choices[0].message.content
