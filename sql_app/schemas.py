from typing import List, Optional

from pydantic import BaseModel, Field, ValidationError, validator


class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str = Field(title="The password of the user", max_length=16, min_length=8)

    # Field level validation
    @validator('password')
    def password_validation(cls, v):
        if 'chaubey' in v:
            raise ValueError('must not contain chaubey')
        return v

    # Object level validation
    @validator('password')
    def passwords_match(cls, v, values, **kwargs):
        if 'chavinay18@gmail' in values.get('email') and 'chaubey18' in v:
            raise ValueError('Email and Password is invalid.')
        return v



class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True
