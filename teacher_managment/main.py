# app/main.py
from fastapi import FastAPI
from routers import teachers, schedules, performance, notifications

app = FastAPI(title="Teacher Dashboard API")

app.include_router(teachers.router)
app.include_router(schedules.router)
app.include_router(performance.router)
app.include_router(notifications.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Teacher Dashboard API"}