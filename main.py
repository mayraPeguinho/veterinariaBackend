from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from exceptions.handler_exepct import app_exception_handler

from routers import auth

app = FastAPI()
app.include_router(auth.router)
app.add_exception_handler(Exception, app_exception_handler)

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
