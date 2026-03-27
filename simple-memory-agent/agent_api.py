from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any, List

from agent import Agent  # Import Agent class from agent.py
from dotenv import load_dotenv
import os

print("LOADED agent_api.py FROM:", __file__)

DEFAULT_MODEL: str = "claude-haiku-4-5-20251001"
load_dotenv()
api_key = (
        os.getenv("ANTHROPIC_API_KEY") or
        os.getenv("GROQ_API_KEY") or
        os.getenv("OPENAI_API_KEY") or
        os.getenv("GEMINI_API_KEY")
    )

app = FastAPI(
    title="Memory Agent API",
    description="Multi-tenant conversational agent with semantic memory",
    version="1.0.0"
)

# Session cache: run_id -> Agent instance
# ONE Agent per session (run_id) maintained in memory
_session_cache: Dict[str, Agent] = {}

def _get_or_create_agent(user_id: str, run_id: str) -> Agent:
    """Get existing Agent for session or create new one."""
    if run_id in _session_cache:
        return _session_cache[run_id]

    # Create new agent for this session
    agent = Agent(user_id=user_id, run_id=run_id, api_key=api_key)
    _session_cache[run_id] = agent
    return agent

# Define Pydantic request/response models here
class PingResponse(BaseModel):
    status: str
    message: str

class InvocationRequest(BaseModel):
    user_id: str = Field(..., description="User identifier for memory isolation")
    run_id: str = Field(..., description="Session identifier for multi-session tracking")
    query: str = Field(..., description="User message to send to the agent")
    model: Optional[str] = Field(DEFAULT_MODEL, description="LLM model to use")

class InvocationResponse(BaseModel):
    status: str
    user_id: str
    run_id: str
    response: str

# Implement /ping and /invocation endpoints
@app.get("/ping", response_model=PingResponse)
def ping():
    return PingResponse(
        status="ok",
        message="Memory Agent API is running"
    )

@app.post("/invocation", response_model=InvocationResponse)
def invoke_agent(req: InvocationRequest):
    try:
        agent = _get_or_create_agent(
            user_id=req.user_id,
            run_id=req.run_id
        )

        response_text = agent.chat(req.query)

        return InvocationResponse(
            status="success",
            user_id=req.user_id,
            run_id=req.run_id,
            response=response_text
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
print("InvocationRequest fields:", InvocationRequest.model_fields.keys())
