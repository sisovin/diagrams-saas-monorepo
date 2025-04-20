from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi
from pydantic import BaseModel, Field, ValidationError

from routes.analytics import router as analytics_router
from routes.auth import router as auth_router
from routes.chat import router as chat_router
from routes.crm import router as crm_router
from routes.files import router as files_router
from routes.generic import router as generic_router
from routes.identity import router as identity_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(analytics_router, prefix="/analytics")
app.include_router(auth_router, prefix="/auth")
app.include_router(chat_router, prefix="/chat")
app.include_router(crm_router, prefix="/crm")
app.include_router(files_router, prefix="/files")
app.include_router(generic_router, prefix="/generic")
app.include_router(identity_router, prefix="/identity")

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Diagrams SaaS API",
        version="1.0.0",
        description="API documentation for Diagrams SaaS",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi
