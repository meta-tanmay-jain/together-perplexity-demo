from database import base
from sqlalchemy import Column, Integer, String, TIMESTAMP,text


class QueryData(base):
    __tablename__ = "query_data"

    id = Column(Integer,primary_key=True,nullable=False,autoincrement=True)
    prompt = Column(String,nullable=False)
    responce = Column(String)
    created_at = Column(TIMESTAMP(timezone=True),server_default=text('now()'))