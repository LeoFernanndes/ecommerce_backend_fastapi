from pydantic import BaseModel


class UserCreateDto(BaseModel):
    first_name: str
    last_name: str
    password: str

    class Config:
        orm_mode = True


class UserResponseDto(BaseModel):
    id: int
    first_name: str
    last_name: str
    password: str

    class Config:
        orm_mode = True
