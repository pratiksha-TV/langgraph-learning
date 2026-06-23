from typing import TypedDict


class AgentState(TypedDict):
    question: str
    agent_type: str
    result: str