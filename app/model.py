from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.orm import declarative_base
from geoalchemy2 import Geography

Base = declarative_base()


class TrafficData(Base):
    __tablename__ = "traffic_data"

    id = Column(Integer, primary_key=True, autoincrement=True)
    geom = Column(Geography("POINT"), nullable=True)
    year = Column(Integer, nullable=True)
    region_id = Column(Integer, nullable=True)
    cars_and_taxis = Column(Integer, nullable=True)
    buses_and_coaches = Column(Integer, nullable=True)
    lgvs = Column(Integer, nullable=True)
    hgvs_2_rigid_axle = Column(Integer, nullable=True)
    hgvs_3_rigid_axle = Column(Integer, nullable=True)
    hgvs_4_or_more_rigid_axle = Column(Integer, nullable=True)
    hgvs_3_or_4_articulated_axle = Column(Integer, nullable=True)
    hgvs_5_articulated_axle = Column(Integer, nullable=True)
    hgvs_6_articulated_axle = Column(Integer, nullable=True)
    all_hgvs = Column(Integer, nullable=True)
    all_motor_vehicles = Column(Integer, nullable=True)
    count_point_id = Column(Integer, nullable=True)
    local_authority_id = Column(Integer, nullable=True)
    easting = Column(Integer, nullable=True)
    northing = Column(Integer, nullable=True)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    link_length_km = Column(Float, nullable=True)
    link_length_miles = Column(Float, nullable=True)
    pedal_cycles = Column(Integer, nullable=True)
    two_wheeled_motor_vehicles = Column(Integer, nullable=True)
    region_name = Column(String, nullable=True)
    region_ons_code = Column(String, nullable=True)
    direction_of_travel = Column(String, nullable=True)
    local_authority_name = Column(String, nullable=True)
    local_authority_code = Column(String, nullable=True)
    road_name = Column(String, nullable=True)
    road_category = Column(String, nullable=True)
    road_type = Column(String, nullable=True)
    start_junction_road_name = Column(String, nullable=True)
    end_junction_road_name = Column(String, nullable=True)
    estimation_method = Column(String, nullable=True)
    estimation_method_detailed = Column(String, nullable=True)
