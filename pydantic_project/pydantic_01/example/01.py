from pydantic import BaseModel

# class User(BaseModel):
#     id : int
#     name: str
#     age: int

# user = User(id = 1 , name="Kabeer", age=22)

# print(user)


class Product(BaseModel):
    pid : int
    pname : str
    price : float
    pstock : bool

p1 = Product(pid=1, pname= "bottle",price= "799", pstock= True)
print(p1)