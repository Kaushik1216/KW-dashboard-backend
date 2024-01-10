from pydantic import BaseModel,Field
from typing import Annotated
from datetime import datetime
from fastapi import Body, FastAPI
from typing import List
# User Model


class Todo(BaseModel):
    title: str
    description: str


class UserModel(BaseModel):
    firstname: str
    lastname: str
    username: str
    email: str
    password: str
    totalcredit: int
    usedcredit: int

# As Model cost may change in future so creating diffrent collection for it help to update model costs


class ModelCost(BaseModel):
    modelname: str
    inrate: float
    outrate: float

# usertoken model

class UserToken(BaseModel):
    modelname: str
    type: str
    Usage: int
    currentrate: float
    timestamp: str = str(datetime.date(datetime.now()))
    inorout: str  # "in" or "out"


# # User token usage model identify by username


class UserTokensModel(BaseModel):
    username: str = Field(..., min_length=3)
    tokens: list[UserToken]

# # Model for Dumy Data of OpenAI responses


# class OpenAiUsage(BaseModel):
#     promt_tokens: int
#     completion_tokens: int
#     total_tokens: int


# class OpenAichoices(BaseModel):
#     message: dict["role": str, "content": str]
#     logprobs: str | None
#     finish_reason: str
#     index: 0


# class OpenAiresponse(BaseModel):
#     id: str
#     object: str
#     created: int
#     model: str
#     usage:  dict = OpenAiUsage
#     choices: list[OpenAichoices]
