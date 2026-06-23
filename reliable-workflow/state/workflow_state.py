from typing import TypedDict


class WorkflowState(TypedDict):
    question: str
    documents: str
    answer: str
    retry_count: int
    error: str
    approval: str