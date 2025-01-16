from fastapi import FastAPI
from app.api.routes import router
from app.db.database import Base, engine

# 初始化数据库
Base.metadata.create_all(bind=engine)

app = FastAPI()

# 包含所有路由
app.include_router(router)