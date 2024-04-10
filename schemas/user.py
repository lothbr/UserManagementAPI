def UserEntity(item) -> dict:
    return {
        "id":str(item["_id"]),
        "firstname": item["firstname"],
        "lastname":item["lastname"],
        "email":item["email"],
        "password": item["password"],
        "username": item["username"]
    }

def UsersEntity(entity) -> list:
    return [UserEntity(item) for item in entity]

def SerializeDict(a)-> dict:
    return {**{i:str(a[i]) for i in a if i=='_id'},**{i:str(a[i]) for i in a if i !='_id'}}

def SerializeList(entity)-> list:
    return [SerializeDict(a) for a in entity]