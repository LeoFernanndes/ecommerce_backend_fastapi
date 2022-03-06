from pydantic import BaseModel


class UserCreateDto(BaseModel):
    first_name: str
    last_name: str
    password: str
