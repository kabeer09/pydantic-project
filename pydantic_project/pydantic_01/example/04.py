from typing import List, Dict, Optional
from pydantic import BaseModel, Field

# class Address_info(BaseModel):
#     House_id: int
#     street: str
#     city: str
#     pincode: str = Field(..., min_length=6)

# class User_info(BaseModel):
#     userid: int
#     username: str
#     useraddress: Address_info

# class Comments(BaseModel):
#     id: int
#     content: str
#     replies: Optional[List['Comments']] = None

# Comments.model_rebuild()

# add = Address_info(
#     House_id=12,
#     street='Alexender Road',
#     city="Berline",
#     pincode='123456'
# )

# user = User_info(
#     userid=2333,
#     username='Alekas somaya',
#     useraddress=add
# )

# comments = [
#     Comments(id=22, content='hi, how are you????')
# ]



class Lesson(BaseModel):
    lesson_id : int
    topic : str

class Module(BaseModel):
    module_id : int
    name : str
    lessons : List[Lesson]

class Course(BaseModel):
    Course_id : int
    name : str
    modules : List[Module]