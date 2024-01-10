from fastapi import FastAPI, HTTPException

from database import registerUser , getAllModelcosts ,getuserusedtoken,loginUser,getUser
from model import UserModel,UserTokensModel
import json
# an HTTP-specific exception class  to generate exception information

from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = [
    "https://kwdashboard.onrender.com/",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"Hello": "World"}

# Api for register new user

@app.post("/api/user/register/", response_model=UserModel)
async def registeruser(userdata: UserModel):
    response = await registerUser(userdata.dict())
    if response:
        return response
    raise HTTPException(400, "Something went wrong")

#Api for login check up
@app.post("/api/user/login/{username}", response_model=UserModel)
async def registeruser(username):
    response = await loginUser(username)
    if response:
        return response
    raise HTTPException(400, "Something went wrong")

#Api to get User data
@app.get("/api/user/data/{username}", response_model=UserModel)
async def getuserdata(username):
    response = await getUser(username)
    if response:
        return response
    raise HTTPException(400, "Something went wrong")

#Api to get all usertokens
@app.get("/api/userstokens/{username}", response_model=UserTokensModel)
async def getuserstoken(username):
    response = await getuserusedtoken(username)
    return response


# API to get all model cost
@app.get("/api/modelcosts/")
async def getmodelcosts():
    response = await getAllModelcosts()
    return response
