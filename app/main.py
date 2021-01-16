import random
from datetime import datetime, timedelta
from typing import Optional

import names
from fastapi import FastAPI, Response, status
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import time

app = FastAPI()

# Allow all origins
origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def hello():
    return "Hello 🌷"


@app.get("/users/taken")
def check_username(username):
    if username == "tulip2014":
        return {"taken": True}

    if username.startswith("slow"):
        time.sleep(4)

    if username == "slow":
        return {"taken": True}

    if username == "error":
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

    if username == "invalidJSON":
        return "this isn't a json :("

    return {"taken": False}
