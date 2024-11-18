# Traffic Data Filtering API

This is a **FastAPI** application designed to filter traffic data. The application integrates with a **Postgres PostGIS** database hosted on AWS **RDS** to retrieve and process traffic data.

---

## 🌐 Live Application

The service is hosted on **AWS Fargate** and can be accessed at the following endpoint:

- **Base URL**: [http://trafficalbv3-1320463290.eu-north-1.elb.amazonaws.com](http://trafficalbv3-1320463290.eu-north-1.elb.amazonaws.com)

---

## 📄 API Documentation

FastAPI automatically generates interactive API documentation, accessible via the following URLs:

- **Swagger UI**: [http://trafficalbv3-1320463290.eu-north-1.elb.amazonaws.com/docs](http://trafficalbv3-1320463290.eu-north-1.elb.amazonaws.com/docs)
- **ReDoc**: [http://trafficalbv3-1320463290.eu-north-1.elb.amazonaws.com/redoc](http://trafficalbv3-1320463290.eu-north-1.elb.amazonaws.com/redoc)

These endpoints provide details on the API's available endpoints, parameters, and responses.

## 🚀 Features

- **Filter Traffic Data**: Perform filtering on traffic data based on parameters: data, road name and radius.
- **Interactive API Documentation**: Test and explore the API using Swagger UI or ReDoc.
- **Cloud Hosted**: Deployed on AWS using Fargate.

---

## ⚙️ Setup and Installation

To set up and run the application locally:

### Prerequisites
1. **Python 3.10+**
2. **Docker** (optional)
3. **Postgres** with **PostGIS** installed (if running a local database).

### Steps
1. Clone the repository:
   ```
   bash
   git clone https://github.com/canderson-13/traffic-api
   cd traffic-api
   ```

2. Create venv:
    ```
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3. Install requirements:
    ```
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    ```

4. Update DB credentials:
    In app/db.py, update the database credentials to access your local database

5. Run the application:
    ```
    uvicorn app.main:app --reload
    ```
    Visit the local development server:
    Base URL: http://127.0.0.1:8000
    Swagger UI: http://127.0.0.1:8000/docs
    ReDoc: http://127.0.0.1:8000/redoc

---

## Deployment:

On a push to the main branch, a github actions workflow will be triggered that builds this docker image, and pushes it to a repo in ECR.

The updated image is then deployed to the AWS Fargate Service.

