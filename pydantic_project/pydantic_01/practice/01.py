from pydantic import BaseModel

class Product(BaseModel):
    id : int
    name : str
    price : float
    stock : bool

product = Product(id=12,name='copper bottle',price=549,stock= True)
print(product)