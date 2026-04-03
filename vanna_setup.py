import os
from dotenv import load_dotenv

# Correct Import Paths for Vanna 2.0
from vanna import Agent
from vanna.core.registry import ToolRegistry
from vanna.core.user import UserResolver, User, RequestContext
from vanna.tools import RunSqlTool, VisualizeDataTool
from vanna.tools.agent_memory import SaveQuestionToolArgsTool, SearchSavedCorrectToolUsesTool, SaveTextMemoryTool
from vanna.servers.fastapi import VannaFastAPIServer
from vanna.integrations.google import GeminiLlmService
from vanna.integrations.sqlite import SqliteRunner
from vanna.integrations.local.agent_memory import DemoAgentMemory

# Load environment variables from the .env file
load_dotenv()

def get_vanna_agent():
    """Initializes and returns the Vanna 2.0 Agent."""
    
    # 1. The Brain: Initialize the LLM Service using Gemini
    gemini_api_key = os.environ.get("GOOGLE_API_KEY")
    if not gemini_api_key:
        raise ValueError("GOOGLE_API_KEY environment variable is missing. Check your .env file.")
        
    llm = GeminiLlmService(api_key=gemini_api_key, model="gemini-3.1-flash-lite-preview")

    # 2. The Connector: Setup the Database Runner
    db_tool = RunSqlTool(
        sql_runner=SqliteRunner(database_path="clinic.db")
    )

    # 3. The Context: Configure Agent Memory
    agent_memory = DemoAgentMemory()

    # 4. Context Management: Create User Resolver
    # Required to identify users in a stateless API environment
    class SimpleUserResolver(UserResolver):
        async def resolve_user(self, request_context: RequestContext) -> User:
            user_email = request_context.get_cookie('vanna_email') or 'guest@example.com'
            group = 'admin' if user_email == 'admin@example.com' else 'user'
            return User(id=user_email, email=user_email, group_memberships=[group])
            
    user_resolver = SimpleUserResolver()

    # 5. The Capabilities: Register Tools
    tools = ToolRegistry()
    tools.register_local_tool(db_tool, access_groups=['admin', 'user'])
    tools.register_local_tool(SaveQuestionToolArgsTool(), access_groups=['admin'])
    tools.register_local_tool(SearchSavedCorrectToolUsesTool(), access_groups=['admin', 'user'])
    tools.register_local_tool(SaveTextMemoryTool(), access_groups=['admin', 'user'])
    tools.register_local_tool(VisualizeDataTool(), access_groups=['admin', 'user'])

    # 6. Assembly: Connect components into the final Agent
    agent = Agent(
        llm_service=llm,
        tool_registry=tools,
        user_resolver=user_resolver,
        agent_memory=agent_memory
    )
    
    return agent

if __name__ == "__main__":
    # Run a quick sanity check
    try:
        agent = get_vanna_agent()
        print("✅ Vanna 2.0 Agent successfully initialized and wired up!")
    except Exception as e:
        print(f"❌ Error initializing agent: {e}")