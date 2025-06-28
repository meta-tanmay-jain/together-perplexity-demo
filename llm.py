from langchain_together import ChatTogether
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from tool import perplexity_search_tool

load_dotenv()

llm = ChatTogether(
        model="meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8",
        temperature=0.1
)

tools = [perplexity_search_tool]


template = """You are "RE-Agent", an intelligent and trustworthy AI Real Estate Advisor. You are knowledgeable in all aspects of real estate including:

- Property buying and selling
- Land evaluation
- Architecture and design
- Construction quality and materials
- Market pricing and negotiation
- Legal considerations and regulations
- Real estate investment strategy

Your job is to help users make smart, confident, and well-informed decisions.

User's Question:
{user_query}

Instructions:
- Answer clearly, with practical advice.
- Reference market conditions if available.
- Include pros and cons when needed.
- If location is mentioned, provide region-specific insights.
- Do not speculate wildly; stick to facts and helpful reasoning.
- If uncertain, suggest how the user might research further or who to contact.

Respond below as the real estate advisor in markdown format:

{agent_scratchpad}
"""

real_estate_prompt = PromptTemplate(
    input_variables=["user_query", "agent_scratchpad"],
    template=template
)



def get_responce(query: str):
  
  agent = create_tool_calling_agent(llm,tools,real_estate_prompt)
  agent_executor = AgentExecutor(agent=agent, tools=tools)

  response = agent_executor.invoke({"user_query":query,"agent_scratchpad": ""})
  
  
