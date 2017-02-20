from werkzeug.security import safe_str_cmp
from models.user import UserModel

def authenticate(username, password):
    user = UserModel.find_by_username(username) # default is None

    if user and safe_str_cmp(user.password , password):
        return user
    else: return None


def identity(payload):
    user_id = payload["identity"]
    return UserModel.find_by_id(user_id)


# {
#   "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE0ODczNTYyMDMsImlkZW50aXR5IjoxLCJpYXQiOjE0ODczNTU5MDMsIm5iZiI6MTQ4NzM1NTkwM30.VHJ3zx5oIiIwuJXQ7H9hsQ6s6FS_8xOGSrQpTpNcauo"
 # }