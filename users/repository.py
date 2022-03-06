from sqlalchemy.orm import Session
from users import dto, models


class UserRepository:
    def __init__(self, sql_alchemy_session: Session):
        self.__sql_alchemy_session = sql_alchemy_session

    def create_user(self, user: dto.UserCreateDto):
        user_table_object = models.User(
            first_name = user.first_name,
            last_name = user.last_name,
            password = user.password
        )
        self.__sql_alchemy_session.add(user_table_object)
        self.__sql_alchemy_session.commit()
        return user_table_object

    def list_users(self):
        return self.__sql_alchemy_session.query(models.User).all()
