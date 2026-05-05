from pydantic import BaseModel, Field
from datetime import datetime
from typing import List

# class Product(BaseModel):
#     product_id: int
#     name: str
#     price: float
    
# class Order(BaseModel):
#     order_id: int
#     product_id: List[Product]
#     total_amount: float
#     created_at: datetime = Field(default_factory=datetime.now)

# # Create product
# product = Product(product_id=11, name='waterbottle', price=799)

# # Create order (FIXED)
# order = Order(
#     order_id=342,
#     product_id=[product],   
#     total_amount=999
#     # created_at auto-filled
# )

# print(order)


# # 🧾 BILL FORMAT
# print("\n========= INVOICE =========")
# print(f"Order ID   : {order.order_id}")
# print(f"Date       : {order.created_at.strftime('%d-%m-%Y %H:%M:%S')}")
# print(f"\nItems     : {order.product_id}") 


# print("\n---------------------------")
# print(f"Total Amount: ₹{order.total_amount}")
# print("===========================\n")




class Address(BaseModel):
    hid : int
    street : str
    city : str
    zipcode : str = Field(...,max_length=6)

class User(BaseModel):
    id : int
    name : str
    email : str
    is_active : bool=True
    createdAt: datetime
    address : Address
    tags : List[str] = []


user = User(id=1,name='Alex',email="Alex@g.com",is_active=True,createdAt=datetime(2015,3,23, 13, 30,30), address= Address(
    hid=1,street="Alexendria Road Hi1",city="Berline",zipcode="23Bj43"), tags=["Premium","Subscriber"]) # type: ignore




py_dict = user.model_dump()
print(py_dict)

print("_________________________________________________________________________________________________________________________________")


json_str = user.model_dump_json()
print(json_str)