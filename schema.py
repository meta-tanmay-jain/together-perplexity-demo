from pydantic import BaseModel
from datetime import datetime

class QueryRequest(BaseModel):
    prompt: str


class QueryResponce(QueryRequest):
    id: int
    responce: str
    created_at: datetime

    class config:
        orm_mode = True
    