from langchain_community.agent_toolkits import create_sql_agent
from langchain_openai import ChatOpenAI
from langchain_community.utilities import SQLDatabase
from sqlalchemy.orm import Session
from .data_context import Sales, BUSINESS_CONTEXT

# Set up the LLM and DB connection
def get_sql_agent_executor(db_session: Session):
    # Ensure you have your OpenAI API Key set as an environment variable
    llm = ChatOpenAI(model="gpt-4o", temperature=0) 
    
    # 1. Initialize SQLDatabase with the SQLAlchemy engine
    # Include all tables relevant to the project
    db = SQLDatabase(
        engine=db_session.bind, 
        include_tables=['sales', 'tickets', 'users']
    )

    # 2. Create the SQL Agent
    agent_executor = create_sql_agent(
        llm=llm,
        db=db,
        agent_type="openai-tools", # Best practice for GPT models
        verbose=True
    )
    
    # Inject custom context into the agent's system prompt
    custom_prompt = (
        "You are an expert Business Insights Co-Pilot. "
        f"Your analysis must be based on the provided data context: {BUSINESS_CONTEXT} "
        "When generating SQL, only use the tables: sales, tickets, users. "
        "Always provide a detailed, natural-language business insight based on the query result, "
        "not just the raw data or the SQL query."
    )
    
    # Override system prompt (depends on LangChain version/Agent type)
    # A cleaner way is to use a custom prompt template, but this illustrates the goal.
    agent_executor.agent.prompt.messages[0].content = custom_prompt
    
    return agent_executor

def generate_insights(question: str, db: Session) -> str:
    """Executes the RAG SQL agent and returns the natural language insight."""
    try:
        agent_executor = get_sql_agent_executor(db)
        
        # The agent runs, writes SQL, executes it, and interprets the result.
        response = agent_executor.invoke({"input": question})
        
        # The final answer is typically in the 'output' key
        return response['output']
    except Exception as e:
        return f"An error occurred while generating insights: {str(e)}"