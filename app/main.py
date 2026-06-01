from fastapi import FastAPI

from app.api.routes.health import router as health_router
from app.api.routes.processing import router as processing_router
from app.api.routes.questions import router as questions_router
from app.api.routes.upload import router as upload_router
from app.api.routes.download import (
    router as download_router
)
from app.api.routes.status import (
    router as status_router
)
from app.api.routes.cleanup import (
    router as cleanup_router
)

app = FastAPI(
    title="Cognitive Offloading API",
    version="1.0",
    description="API for processing questions and answers with cognitive offloading"
)

# Register routers
app.include_router(health_router)
app.include_router(processing_router)
app.include_router(questions_router)
app.include_router(upload_router)
app.include_router(download_router)
app.include_router(status_router)
app.include_router(cleanup_router)