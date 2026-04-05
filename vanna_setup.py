import os
from dotenv import load_dotenv

from vanna import Agent
from vanna.core.registry import ToolRegistry
from vanna.core.user import UserResolver, User, RequestContext
from vanna.tools import RunSqlTool, VisualizeDataTool
from vanna.tools.agent_memory import SaveQuestionToolArgsTool, SearchSavedCorrectToolUsesTool, SaveTextMemoryTool
from vanna.integrations.openai import OpenAILlmService
from vanna.integrations.sqlite import SqliteRunner
from vanna.integrations.local.agent_memory import DemoAgentMemory

load_dotenv()

def validate_sql(sql: str) -> tuple[bool, str]:
    sql_upper = sql.upper().strip()
    if not sql_upper.startswith("SELECT"): return False, "Security Error: Only SELECT queries are allowed."
    dangerous_keywords = ["INSERT", "UPDATE", "DELETE", "DROP", "ALTER", "EXEC", "XP_", "SP_", "GRANT", "REVOKE", "SHUTDOWN"]
    for word in dangerous_keywords:
        if word in sql_upper: return False, f"Security Error: Dangerous keyword '{word}' detected."
    if "SQLITE_MASTER" in sql_upper: return False, "Security Error: Access to system tables is forbidden."
    return True, "Valid"

class SafeSqliteRunner(SqliteRunner):
    async def run_sql(self, args, context):
        # Extract the SQL string from the args object
        sql_string = args.sql
        
        # Run our security validation
        is_valid, msg = validate_sql(sql_string)
        if not is_valid:
            # Raise an exception so Vanna's tool engine catches it
            raise ValueError(f"SQL Validation Failed: {msg}")
            
        # Pass the original args and context back to the parent class asynchronously
        return await super().run_sql(args, context)


def get_vanna_agent():
    groq_api_key = os.environ.get("GROQ_API_KEY")
    if not groq_api_key: 
        raise ValueError("Missing GROQ_API_KEY")

    llm = OpenAILlmService(
        model="openai/gpt-oss-20b",
        api_key=groq_api_key,
        base_url="https://api.groq.com/openai/v1"
    )

    # Connect our Safe Runner that intercepts bad queries
    db_tool = RunSqlTool(
        sql_runner=SafeSqliteRunner(database_path="clinic.db")
    )

    agent_memory = DemoAgentMemory()

    class SimpleUserResolver(UserResolver):
        async def resolve_user(self, request_context: RequestContext) -> User:
            return User(id="admin_user", username="admin", email="admin@example.com", group_memberships=['admin'])
            
    tools = ToolRegistry()
    tools.register_local_tool(db_tool, access_groups=['admin', 'user'])
    tools.register_local_tool(SaveQuestionToolArgsTool(), access_groups=['admin'])
    tools.register_local_tool(SearchSavedCorrectToolUsesTool(), access_groups=['admin', 'user'])
    tools.register_local_tool(SaveTextMemoryTool(), access_groups=['admin', 'user'])
    tools.register_local_tool(VisualizeDataTool(), access_groups=['admin', 'user'])

    agent = Agent(llm_service=llm, tool_registry=tools, user_resolver=SimpleUserResolver(), agent_memory=agent_memory)
    return agent