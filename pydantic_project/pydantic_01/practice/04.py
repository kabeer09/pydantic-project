from pydantic import BaseModel, computed_field
from typing import List, Optional

class Product(BaseModel):
    product_id : int
    name : str
    price : float
    
class Order(BaseModel):
    order_id : int
    product_id : List[Product]
    total_amount : float

class User(BaseModel):
    name : str
    address : str
    order_id : Order
    total_amount : Order
    
   
    


    
