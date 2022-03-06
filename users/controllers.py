from typing import List
from users.repository import UserRepository
from users.dto import UserCreateDto
from users.models import User


class UserController:
    def __init__(self, user_repository: UserRepository):
        self.__user_repository = user_repository

    async def create_user(self, user: UserCreateDto) -> User:
        return self.__user_repository.create_user(user)

    async def list_users(self) -> List[User]:
        return self.__user_repository.list_users()
