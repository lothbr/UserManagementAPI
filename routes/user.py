from fastapi import APIRouter
from Models.user import User,Login
from config.db import conn
from schemas.user import UserEntity,UsersEntity
from bson import ObjectId

user = APIRouter()

@user.get('/Get_all_Users')
async def GetAllUsers():
    print(conn.local.user.find())
    print(UsersEntity(conn.local.user.find()))
    return UsersEntity(conn.local.user.find())

@user.get('/{id}')
async def find_user(id):
    return UserEntity(conn.local.user.find_one({"_id":ObjectId(id)}))

@user.post('/Create_new_User')
async def createUser(user:User):
    conn.local.user.insert_one(dict(user))
    return UsersEntity(conn.local.user.find())

@user.put('/{id}')
async def update_user(id,user: User):
    conn.local.user.find_one_and_update(
        {"_id":ObjectId(id)}, {"$set":dict(user)}
        )
    return UserEntity(conn.local.user.find_one({"_id":ObjectId(id)}))

@user.delete('/{id}')
async def delete_user(id):
    return UserEntity(conn.local.user.find_one_and_delete({"_id":ObjectId(id)}))
