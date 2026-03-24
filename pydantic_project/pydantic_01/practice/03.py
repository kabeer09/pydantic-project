from pydantic import BaseModel, Field, field_validator, model_validator, computed_field #type: ignore

class Booking(BaseModel):
    user_id : int
    room_id : int
    nights : int = Field(...,ge=1)
    rate_per_night : float
    
    @computed_field
    @property
    
    def Calculate_price(self):
        return self.nights * self.rate_per_night
        
    
   
    