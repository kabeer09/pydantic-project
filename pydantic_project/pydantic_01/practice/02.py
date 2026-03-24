from pydantic import BaseModel, Field
from typing import Optional

class Employee(BaseModel):
    id : int
    info : str = Field(...,min_length=10,max_length=50,discriminator="Employee Information",examples="Bottle")
    department : Optional[str] = 'General'
    salary : float = Field(..., ge= 10000)