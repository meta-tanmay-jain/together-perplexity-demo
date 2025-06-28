from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import List

from database import engine, Base, Query, get_db
from schema import QueryRequest, QueryResponse
from llm import get_response

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Real Estate AI Advisor")

@app.post("/chat", response_model=QueryResponse)
def chat(request: QueryRequest, db: Session = Depends(get_db)):
    """Chat with the Real Estate AI Advisor"""
    
    ai_response = get_response(request.prompt)
    
    query = Query(prompt=request.prompt, response=ai_response)
    db.add(query)
    db.commit()
    db.refresh(query)
    
    return query

@app.get("/history", response_model=List[QueryResponse])
def get_history(page: int = 1, limit: int = 10, db: Session = Depends(get_db)):
    """Get chat history with pagination"""
    
    offset = (page - 1) * limit
    queries = db.query(Query).offset(offset).limit(limit).all()
    return queries

@app.get("/")
def root():
    return {"message": "Real Estate AI Advisor API"}