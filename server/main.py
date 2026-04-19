from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from middlewars.exception_handlers import catch_exception_middleware
from routes.upload_pdfs import router as upload_router
from routes.ask_questions import router as ask_router

app=FastAPI(title="Medical Assistant Api",description="API for AI Medical Assissant chatBot")

# CORS Setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

#middle exception handlers
app.middleware("http")(catch_exception_middleware)

#routers
#1.Upload pdf documents
app.include_router(upload_router)

#2. Asking query
app.include_router(ask_router)