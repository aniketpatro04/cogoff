from fastapi import FastAPI

from app.api.routes.health import router as health_router
from app.api.routes.processing import router as processing_router
from app.api.routes.questions import router as questions_router

app = FastAPI(
    title="Cognitive Offloading API",
    version="1.0",
    description="API for processing questions and answers with cognitive offloading"
)

# Register routers
app.include_router(health_router)
app.include_router(processing_router)
app.include_router(questions_router)