from pydantic import BaseModel
from datetime import datetime

class QueryRequest(BaseModel):
    prompt: str

class QueryResponse(BaseModel):
    id: int
    prompt: str
    response: str
    created_at: datetime
    
    class Config:
        from_attributes = True