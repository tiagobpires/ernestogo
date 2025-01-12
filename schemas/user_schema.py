from pydantic.v1 import BaseModel
from typing import Optional


class SearchUser(BaseModel):
    search: str = ""
    page: int = 1


class UserCreate(BaseModel):
    username: str
    email: str
    description: Optional[str]


class UserResponse(UserCreate):
    id: int

    class Config:
        orm_mode = True


class UserListResponse(BaseModel):
    page: int
    pages: int
    total: int
    users: list[UserResponse]
