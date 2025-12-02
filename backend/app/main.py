from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from .database import get_db
from .rag_engine import generate_insights
from fastapi.middleware.cors import CORSMiddleware # Required for React communication

app = FastAPI(title="AI Business Insights Co-Pilot")

# Configure CORS for React development server (adjust in production)
origins = [
    "http://localhost:3000",  # Default React port
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    query: str

class InsightResponse(BaseModel):
    insight: str

@app.get("/api/health")
def health_check():
    return {"status": "ok", "service": "FastAPI Co-Pilot Backend"}

@app.post("/api/rag_insights", response_model=InsightResponse)
def get_ai_insight(
    request: QueryRequest, 
    db: Session = Depends(get_db)
):
    """
    Main endpoint for RAG-driven natural language querying.
    """
    insight = generate_insights(request.query, db)
    return InsightResponse(insight=insight)

# Placeholder for future traditional metrics endpoint
@app.get("/api/metrics/sales_trend")
def get_sales_trend():
    # Placeholder: fetch data directly from DB using Pandas/SQLAlchemy
    # and return structured JSON for a chart.
    return [
        {"month": "Jan", "revenue": 120000},
        {"month": "Feb", "revenue": 150000},
        # ... more data
    ]