from pydantic import BaseModel

class User(BaseModel):
    id : int
    name: str
    age: int

user = User(id = 1 , name="Kabeer", age=22)

print(user)