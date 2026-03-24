from pydantic import BaseModel
from typing import List,Dict,Optional

class ProductCart(BaseModel):
    user_id : int
    items : List[str]
    quntaty : Dict[str, int]
    image_url : Optional[str] = None
    
cart = ProductCart(user_id=112,items=['bottle','glass'],quntaty={'bottle':5,'glass':5},image_url='https//:www.google.com')
print(cart)
    
