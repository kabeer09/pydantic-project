from pydantic import BaseModel,Field, field_validator, model_validator, computed_field #type: ignore

# class User(BaseModel):
#     username : str
    
    
#     @field_validator('username')
    
#     def username_len(cls,v):
#         if len(v) <= 4:
#             raise ValueError("UserName more than 4 character")
#         return v

# class SingUpdata(BaseModel):
    
#     password : str
#     confirm_password : str
    
#     @model_validator(model = 'after')
    
#     def password_matches(cls,Values):
#         if Values.password != Values.confirm_password:
#             raise ValueError("Please Check Password")
#         return Values
    
# class Product(BaseModel):
#     name : str
#     price : float
#     quntity : int
    
#     @computed_field
#     @property
    
#     def Calculate_total_price(self):
#         return self.price * self.quntity
        


class Booking(BaseModel):
    user_id : int
    room_id : int
    nights : int = Field(...,ge=1)
    rate_per_night : float

    @computed_field
    @property
    
    def total_amount(self) -> float: # type: ignore
        return  self.nights * self.rate_per_night
