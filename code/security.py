from werkzeug.security import safe_str_cmp
from user import User

users = [
   User(1,"bob" , "asdf")
]

username_mapping = { u.username: u for u in users}

userid_mapping = { u.id: u for u in users }

def authenticate(username, password):
    user = User.find_by_username(username) # default is None

    if user and safe_str_cmp(user.password , password):
        return user
    else: return None


def identity(payload):
    user_id = payload["identity"]
    return User.find_by_id(user_id)


# {
#   "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE0ODczNTYyMDMsImlkZW50aXR5IjoxLCJpYXQiOjE0ODczNTU5MDMsIm5iZiI6MTQ4NzM1NTkwM30.VHJ3zx5oIiIwuJXQ7H9hsQ6s6FS_8xOGSrQpTpNcauo"
 # }