from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import word
from app.database.database import Base, engine

app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(word.router)

#@app.get("/")
#def Hello():
#    return {"Hello":"World!"}