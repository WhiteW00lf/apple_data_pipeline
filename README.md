# Market Data Analytics Pipeline (AAPL)

## Overview
End-to-end data engineering pipeline that ingests daily equity market data for Apple Inc. (AAPL), stores immutable raw data in Google Cloud Storage, and models analytics-ready tables in BigQuery.

Orchestrated with Apache Airflow and designed using production data engineering best practices.

---

## Architecture
 ```
 Market Data API
↓
Airflow (Docker)
↓
GCS (Raw Data Lake)
↓
BigQuery External Tables
↓
BigQuery Fact Tables

```


---

## Tech Stack
- Apache Airflow
- Google Cloud Storage
- BigQuery
- Python, SQL
- Docker
- GCP

---

## Key Features
- Execution-date driven ingestion  
- Idempotent raw data loads  
- Market calendar & timezone handling  
- External → native BigQuery modeling  
- Partitioned analytics tables  

---

## Example Analytics
- High-volume trading days
- Daily Market(AAPL) Mood trend

---

## Status
✅ Raw ingestion  
✅ BigQuery staging  
✅ Analytics fact tables  
