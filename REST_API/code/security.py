users = [
    {
        "id": 1,
        "username":"bob",
        "password":"asdfg"
    }
]

username_mapping = {
    "bob" :  {
        "id": 1,
        "username":"bob",
        "password":"asdfg"
    }
}

userid_mapping = {
    1 :  {
        "id": 1,
        "username":"bob",
        "password":"asdfg"
    }
}

def authenticate(username, password):
    user = username_mapping(username, None) # default is None

    if user and user.password == password:
        return user
    else: return None



def indentify(payload):
    user_id = payload["identity"]
    return userid_mapping.get(user_id,None)