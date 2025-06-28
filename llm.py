from langchain_together import ChatTogether
from langchain.tools import tool
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from perplexity import search_perplexity

load_dotenv()

llm = ChatTogether(
    model="meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8",
    temperature=0.1
)

@tool
def perplexity_tool(query: str) -> str:
    """Search for real-time real estate data"""
    return search_perplexity(query)

prompt = PromptTemplate(
    input_variables=["user_query", "agent_scratchpad"],
    template="""You are a Real Estate AI Advisor. Help users with:
- Property buying/selling
- Market analysis
- Investment advice
- Legal considerations

User Question: {user_query}

Provide clear, practical advice in markdown format.

{agent_scratchpad}"""
)

def get_response(query: str) -> str:
    """Get AI response for real estate query"""
    
    agent = create_tool_calling_agent(llm, [perplexity_tool], prompt)
    executor = AgentExecutor(agent=agent, tools=[perplexity_tool])
    
    result = executor.invoke({
        "user_query": query,
        "agent_scratchpad": ""
    })
    
    return result["output"]