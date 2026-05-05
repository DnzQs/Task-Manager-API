# Task Manager API
A backend REST API for managing tasks with user authentication.

Description:
This project is a RESTful API built with FastAPI that allows users to:

register and authenticate (JWT)
create, read, update, and delete tasks
access only their own data
use filtering and pagination

# Tech Stack:
FastAPI
PostgreSQL
SQLAlchemy
Pydantic
JWT (python-jose)
Docker

# Features:
Authentication
User registration
Login
JWT-based authentication
Tasks
Create task
Get user tasks
Update task
Delete task
Filter by title
Pagination (limit / offset)

# Project structure:
app/
routes/
db.py
main.py
models.py
schemas.py
utils.py

# Run the Project
*Locally
pip install -r requirements.txt
uvicorn app.main:app --reload

# Using Docker
chose the directory where file downloaded
docker-compose up --build

# API Documentation
After running the server:
http://localhost:8000/docs

# Authentication
Use Bearer Token:
Authorization: Bearer <your_token>

#Environment Variables
Create a .env file based on .env.example:

DATABASE_URL=postgresql://postgres:postgres@db:5432/task_manager_db
SECRET_KEY=your_secret_key
