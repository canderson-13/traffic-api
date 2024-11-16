import logging
import os
from sqlalchemy.orm import Session
from typing import List
from fastapi import HTTPException
from app.schema import TrafficDataResponse


def execute_query(db: Session, select_stmt) -> List[TrafficDataResponse]:
    try:
        results = db.execute(select_stmt).scalars().all()
    except Exception as e:
        db.rollback()
        logging.error(f"Database query failed: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

    return [TrafficDataResponse.model_validate(row) for row in results]


def get_docs() -> str:
    docs_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "docs.md")
    )
    try:
        with open(docs_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return "Traffic data API helps you filter traffic data. 🚀"
