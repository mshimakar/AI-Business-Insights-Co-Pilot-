# A simplified, illustrative SQLAlchemy model for the LangChain agent
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Sales(Base):
    __tablename__ = "sales"
    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String)
    region = Column(String)
    revenue = Column(Float)
    sale_date = Column(DateTime)
    
# In a real app, you would define your business logic/definitions
# in separate text files, embed them, and use a vector store.
# For simplicity, we are focusing on the SQL integration here.
BUSINESS_CONTEXT = (
    "The primary goal is to analyze Sales, Tickets, and User data. "
    "To calculate average sales per user, you must join the 'sales' "
    "and 'users' tables on 'user_id'."
)