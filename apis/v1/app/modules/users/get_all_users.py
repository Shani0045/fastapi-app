
async def get_users(**kwargs):
    username = kwargs.get("username")
    age = kwargs.get("age")
    users ={"username": username, "age": age}
    return users
