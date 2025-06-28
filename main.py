from typing import List
from fastapi import FastAPI, Depends, Path
from sqlalchemy.orm import Session
from database import engine, SessionLocal
from models import base, QueryData
from schema import QueryRequest, QueryResponce
import llm



base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close

@app.post("/get-response", response_model=List[QueryResponce])
def generate_responce(user_query: QueryRequest, db:Session = Depends(get_db)):
    
    query_response = llm.get_responce(user_query.prompt)

    response_text = query_response.choices[0].message.content 
    
    new_query = QueryData(prompt = user_query.prompt,responce = response_text)
    db.add(new_query)
    db.commit()
    db.refresh(new_query)
    return [new_query]
    
@app.get("/show-responses/{page}", response_model=List[QueryResponce])
def get_responses(page: int = Path(..., ge=1),limit: int = 10, db:Session = Depends(get_db)):
    offset = (page - 1) * limit
    responces = db.query(QueryData).offset(offset).limit(limit).all()
    return responces



