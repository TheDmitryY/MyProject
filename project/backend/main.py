from contextlib import asynccontextmanager
import uvicorn
from fastapi import FastAPI
from app.api.v1 import router as api_v1_router
from app.core.middlewares.request import RequestIdMiddleware, SyncStatusCodeMiddleware
from app.core.configs.database import create_db_and_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize database tables
    await create_db_and_tables()
    yield

app = FastAPI(title="Web Labs Project", lifespan=lifespan)

# Register middlewares
app.add_middleware(RequestIdMiddleware)
app.add_middleware(SyncStatusCodeMiddleware)

# Include routers
app.include_router(api_v1_router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Welcome to Web Labs API"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
