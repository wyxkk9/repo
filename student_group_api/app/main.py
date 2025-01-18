from fastapi import FastAPI
from app.db.database import init_db
from app.api import routes

app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(routes.router)