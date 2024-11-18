from fastapi.testclient import TestClient
from unittest.mock import MagicMock
from sqlalchemy.orm import Session
from app.main import app
from app.db import get_db
from app.model import TrafficData


class MockDBSession:
    def __init__(self):
        self.mock_db = MagicMock(spec=Session)

        self.mock_query_result = MagicMock()
        self.mock_query_result.scalars.return_value.all.return_value = [
            TrafficData(id=1, year=2020, road_name="M25", cars_and_taxis=100),
            TrafficData(id=2, year=2021, road_name="A1", cars_and_taxis=150),
        ]

        self.mock_db.execute.return_value = self.mock_query_result

        self.mock_db.rollback.return_value = None

    def execute(self, select_stmt):
        return self.mock_db.execute(select_stmt)

    def rollback(self):
        return self.mock_db.rollback()


client = TestClient(app)
app.dependency_overrides.update({get_db: lambda: MockDBSession()})


def test_get_date_filtered_data_success():
    response = client.get("/data/date?start=2020&end=2021")

    assert response.status_code == 200

    response_data = response.json()
    assert len(response_data) == 2
    assert response_data[0]["year"] == 2020
    assert response_data[1]["year"] == 2021


def test_get_date_filtered_data_invalid_start_gt_end():
    response = client.get("/data/date?start=2023&end=2020")

    assert response.status_code == 400
    assert response.json() == {
        "detail": "Start year must not be greater than end year."
    }


def test_get_date_filtered_data_invalid_year_start():

    response = client.get("/data/date?start=1999&end=2020")

    assert response.status_code == 422


def test_get_date_filtered_data_invalid_year_end():

    response = client.get("/data/date?start=2020&end=2025")

    assert response.status_code == 422
