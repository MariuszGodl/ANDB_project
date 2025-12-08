# 🗄️ Database Documentation - Scholarship Application System

## 1. Technical Overview
This module handles data persistence for the Scholarship Portal using a **PostgreSQL 15** database containerized with **Docker**. It stores student profiles, application forms, file metadata, and audit logs.

### Connection Details
* **Engine:** PostgreSQL 15
* **Host:** `localhost`
* **Port:** `5433` (Mapped from container port 5432 to avoid local conflicts)
* **Database Name:** `scholarship_app`
* **Username:** `admin`
* **Password:** `password123`

---

## 2. Quickstart Guide
To start the database, ensure **Docker Desktop** is running.

```bash
# Start the database container in detached mode
docker-compose up -d