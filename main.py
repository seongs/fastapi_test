from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from domain.question import question_router

app = FastAPI()


origins = [
    "http://192.168.32.42:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# @app.get("/hello")
# def hello():
#     return{"message": "안녕하세요 파이보"}

app.include_router(question_router.router)

