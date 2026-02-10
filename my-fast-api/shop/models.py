from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field, field_validator


class UserCreate(BaseModel):
    name : str = Field(...,min_length= 3)
    email : str = Field(...,pattern= r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    age : int = Field(...,ge= 0 , le= 100)

    @field_validator('email')
    def validate_email(cls , v : str)-> str:        #custome validator lower wenwa email eka
        return v.lower()

    @field_validator('age')
    def validate_age(cls , a :int)->int:
        if a < 13 :
            raise ValueError('age is lower')
        else:
            return a

class UserResponse(UserCreate):
    id : int
    created_at : datetime
    updated_at : datetime

class UserPatch(BaseModel):
    name: Optional[str] = Field (None, min_length= 3)
    email: Optional[str] = Field (None, pattern= r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    age: Optional[int] = Field (None, ge = 0, le = 100)

    @field_validator('age')
    def validate_age(cls, a: int) -> int:
        if a < 13:
            raise ValueError('age is lower')
        else:
            return a

class ProductCreate(BaseModel):
    name : str = Field(..., min_length=2 , max_length=100)
    description : str = Field(..., min_length=1,max_length=300)
    price : float = Field(..., ge=0)
    category : str = Field(..., min_length=2 , max_length=100)
    tags : List[str] = Field(default_factory=list)

    @field_validator('tags')
    def validate_tags( cls , t : str)-> str:
        if len(t) > 10 :
            raise ValueError('10 tags only you can add')
        else:
            return t

class ProductResponse(ProductCreate):
    id : int
    created_at : datetime
    updated_at : datetime

class ProductPatch(BaseModel):

        name: Optional[str] = Field(..., min_length=2, max_length=100)
        description: Optional[str] = Field(..., min_length=1, max_length=300)
        price: Optional[float] = Field(..., ge=0)
        category: Optional[str] = Field(..., min_length=2, max_length=100)
        tags: Optional[List[str]] = Field(default_factory=list)