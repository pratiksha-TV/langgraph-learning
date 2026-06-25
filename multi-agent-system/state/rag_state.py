from typing import TypedDict


class AgenticRAGState(TypedDict):
    question: str
    retry_count: int
    error: str
    need_retrieval: bool
    retriever_result: str
    web_result: str
    answer: str
    sources: list[str]
    approval: str