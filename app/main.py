from typing import List
from sqlalchemy import select, between
from typing_extensions import Annotated
from fastapi import Depends, FastAPI, HTTPException, Query
from sqlalchemy.orm import Session
from geoalchemy2 import functions as geofunc
from geoalchemy2.shape import from_shape
from shapely.geometry import Point

from app.db import get_db
from app.model import TrafficData
from app.schema import TrafficDataResponse
from app.utils import execute_query, get_docs


app = FastAPI(
    title="Traffic data API",
    description=get_docs(),
    version="0.0.1",
)


@app.get("/data/date", tags=["data"], response_model=List[TrafficDataResponse])
async def get_date_filtered_data(
    start: Annotated[
        int,
        Query(description="Start Year example: 2020", ge=2000, le=2024),
    ],
    end: Annotated[
        int,
        Query(description="End Year example: 2024", ge=2000, le=2024),
    ],
    db: Session = Depends(get_db),
):
    if start > end:
        raise HTTPException(
            status_code=400, detail="Start year must not be greater than end year."
        )
    select_stmt = (
        select(TrafficData).where(between(TrafficData.year, start, end)).limit(5)
    )
    return execute_query(db, select_stmt)


@app.get("/data/road", tags=["data"], response_model=List[TrafficDataResponse])
async def get_road_filtered_data(
    name: Annotated[
        str,
        Query(
            description="Road Name (case insensitive) example: M25",
            min_length=1,
            max_length=50,
        ),
    ],
    db: Session = Depends(get_db),
):
    name = name.strip()
    select_stmt = select(TrafficData).filter(TrafficData.road_name.ilike(name)).limit(5)
    return execute_query(db, select_stmt)


@app.get("/data/radius", tags=["data"], response_model=List[TrafficDataResponse])
async def get_geo_radius_filtered_data(
    long: Annotated[
        float,
        Query(description="Longitude example: 0.12", le=180, ge=-180),
    ],
    lat: Annotated[
        float,
        Query(description="Latitude example:. 51.5", le=90, ge=-90),
    ],
    radius: Annotated[
        float,
        Query(description="Radius in km example: 2.5", le=500, gt=0),
    ],
    db: Session = Depends(get_db),
):
    point = from_shape(Point(long, lat), srid=4326)
    select_stmt = (
        select(TrafficData)
        .filter(geofunc.ST_DWithin(TrafficData.geom, point, radius * 1000))
        .limit(5)
    )
    return execute_query(db, select_stmt)


# TODO: monitoring, alerting, documentation, rate limiting, paging
