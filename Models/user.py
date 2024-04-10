from pydantic import BaseModel

class User(BaseModel):
    firstname: str
    lastname: str
    email:str
    username: str
    password: str

class Login(BaseModel):
    username: str
    password:str