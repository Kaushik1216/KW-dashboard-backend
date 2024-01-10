import motor.motor_asyncio
from model import UserModel, ModelCost

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017/')
database = client.knowwizeDashboard

# Collections in Database
userCollection = database.users
modelcostCollection = database.modelcosts
usertokenusedCollection = database.usersusedtoken
openairesponseCollection = database.openairesponseCollection


# User collection controllers

async def registerUser(user):
    document = user
    result = await userCollection.insert_one(user)
    return document


async def loginUser(username):
    document = await userCollection.find_one({"username": username})
    return document

async def getUser(username):
    document = await userCollection.find_one({"username": username})
    return document

async def fetchAllModelCost():
    documents = []
    cursor = modelcostCollection.find({})
    async for document in cursor:
        documents.append(modelcostCollection(**document))
    return documents


async def getAllUserTokens(username):
    document = await usertokenusedCollection.find_one({"username": username})
    return document


async def getAllModelcosts():
    modelcosts = []
    cursor = modelcostCollection.find({})
    async for document in cursor:
        modelcosts.append(ModelCost(**document))
    return modelcosts

async def getuserusedtoken(username):
    document = await usertokenusedCollection.find_one({"username": username})
    return document

# async def addUserUsedToken(username):
   