from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from domain.question import question_router

app = FastAPI()


@app.get("/hello")
def hello():
    return{"message": "안녕하세요 파이보"}


# origins = [
#     "http://127.0.0.1:5173"
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentail=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )