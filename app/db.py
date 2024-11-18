import boto3
import os
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from typing import Generator


def get_db() -> Generator[Session, None, None]:
    try:
        region = os.getenv("AWS_REGION")
        if not region:
            raise ValueError("AWS_REGION environment variable is missing.")

        secrets_client = boto3.client("secretsmanager", region_name=region)

        secret_arn = os.getenv("DB_SECRET_ARN")
        if not secret_arn:
            raise ValueError("DB_SECRET_ARN environment variable is missing.")

        response = secrets_client.get_secret_value(SecretId=secret_arn)

        secret = None
        if "SecretString" in response:
            secret = json.loads(response["SecretString"])
        elif "SecretBinary" in response:
            secret = json.loads(response["SecretBinary"])

        if not secret:
            raise ValueError("Failed to parse the secret.")

        username = secret.get("username")
        password = secret.get("password")
        host = secret.get("host")
        port = secret.get("port")
        database = secret.get("dbname")

        if not all([username, password, host, port, database]):
            raise ValueError("Missing required fields in the secret.")

        engine = create_engine(
            f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}"
        )
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        db = SessionLocal()

        try:
            yield db
        finally:
            db.close()

    except Exception as e:
        print(f"Error: {e}")
        raise
