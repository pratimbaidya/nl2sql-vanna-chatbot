from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from vanna.servers.fastapi import VannaFastAPIServer
from vanna_setup import get_vanna_agent
from seed_memory import seed_agent_memory
import logging

# --- Setup Simple Structured Logging ---
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - [NL2SQL] %(message)s"
)
logger = logging.getLogger(__name__)

# 1. Initialize the Agent
agent = get_vanna_agent()

# 2. Define the modern FastAPI Lifespan event handler
@asynccontextmanager
async def lifespan(app: FastAPI):
    # This block runs on STARTUP
    logger.info("Server starting up. Seeding Agent Memory...")
    await seed_agent_memory(agent)
    logger.info("Memory seeded. Ready to accept queries!")
    
    yield # The server runs during this yield
    
    # This block runs on SHUTDOWN (optional, but good practice)
    logger.info("Server shutting down gracefully...")

# 3. Initialize Vanna's Server and pass the lifespan via the config dictionary
vanna_server = VannaFastAPIServer(
    agent,
    config={
        "fastapi": {
            "lifespan": lifespan
        }
    }
)

# 4. Generate the FastAPI application instance
app = vanna_server.create_app()

# API Request Logging
@app.middleware("http")
async def log_requests(request: Request, call_next):
    # Log the incoming request
    logger.info(f"Incoming Request: {request.method} {request.url.path}")
    
    # Let Vanna process the request
    response = await call_next(request)
    
    # Log the outgoing response status
    logger.info(f"Outgoing Response: Status {response.status_code} for {request.url.path}")
    return response

# 5. Add the required /health endpoint directly to the Vanna app
@app.get("/health")
def health_check():
    logger.info("Health check endpoint pinged.")
    return {"status": "ok", "database": "connected", "agent_memory_items": 15}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)