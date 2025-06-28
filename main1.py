from together import Together

client = Together(api_key="a2ee2598d775c8c85d6030a021e05a62b07266e635802df9d713b9c872bace47") # auth defaults to os.environ.get("TOGETHER_API_KEY")


query = "Is melody chocolaty?"
response = client.chat.completions.create(
    model="meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8",
    messages=[
      {
        "role": "user",
        "content": f"{query}, please give me the result in markdown format"      }
    ]
)
print(response.choices[0].message.content)