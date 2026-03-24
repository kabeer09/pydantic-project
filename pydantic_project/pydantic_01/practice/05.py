from pydantic import BaseModel, field_validator

class Singup(BaseModel):
    email : str
    password : str
    
    
    @field_validator('email')
    
    def validate_email(cls,values):
        if '@' not in values:
            raise ValueError("Email Not valide")
        return values
        
    def validate_password(cls,values):
        if len(values) < 10:
            raise ValueError("Invalid Password")
        return values


singup = Singup(email='kg@.com',password='ka098765')
print(singup)
        
    
    
