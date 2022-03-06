from fastapi import APIRouter
from database_connections.mysql_database_connection import SessionLocal as mysql_session
from users.repository import UserRepository
from users.controllers import UserController
from users.dto import UserCreateDto

router = APIRouter(prefix='/users')

database_session = mysql_session()
user_repository = UserRepository(database_session)
user_controller = UserController(user_repository)

@router.get('/')
async def list_users():
    response = await user_controller.list_users()
    return response

@router.post('/')
async def create_user(user: UserCreateDto):
    response = await user_controller.create_user(user)
    return response
