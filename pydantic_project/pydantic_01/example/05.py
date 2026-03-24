from pydantic import BaseModel, Field
from datetime import datetime
from typing import List

class Product(BaseModel):
    product_id: int
    name: str
    price: float
    
class Order(BaseModel):
    order_id: int
    product_id: List[Product]
    total_amount: float
    created_at: datetime = Field(default_factory=datetime.now)

# Create product
product = Product(product_id=11, name='waterbottle', price=799)

# Create order (FIXED)
order = Order(
    order_id=342,
    product_id=[product],   
    total_amount=999
    # created_at auto-filled
)

print(order)


# 🧾 BILL FORMAT
print("\n========= INVOICE =========")
print(f"Order ID   : {order.order_id}")
print(f"Date       : {order.created_at.strftime('%d-%m-%Y %H:%M:%S')}")
print(f"\nItems     : {order.product_id}") 


print("\n---------------------------")
print(f"Total Amount: ₹{order.total_amount}")
print("===========================\n")