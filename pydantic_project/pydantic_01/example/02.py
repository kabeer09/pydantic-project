from pydantic import BaseModel,Field
from typing import List,Dict,Optional

# class ProductCart(BaseModel):
#     user_id : int
#     items : List[str]
#     quntaty : Dict[str, int]
#     image_url : Optional[str] = None
    
# cart = ProductCart(user_id=112,items=['bottle','glass'],quntaty={'bottle':5,'glass':5},image_url='https//:www.google.com')
# print(cart)
    

class Employee(BaseModel):
    emp_id : int
    name : str = Field(
        ...,
        min_length=5,
        max_length=50,
        description="Hello")
    department : Optional[str] = 'General'
    salary : float = Field(ge=10000)

employee = Employee(emp_id=1, name= "kabeer", department="aiml",salary=10000)
print(employee)