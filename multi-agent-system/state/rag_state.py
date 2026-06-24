from typing import TypedDict


class AgenticRAGState(TypedDict):
    question: str
    need_retrieval: bool
    documents: str
    answer: str
    sources: list[str]
    approval: str