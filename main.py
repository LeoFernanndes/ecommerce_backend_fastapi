import datetime
import uvicorn
from fastapi import FastAPI
from users import models as users_models
from database_connections.mysql_database_connection import engine
from users import routes as user_routes
from decouple import config


app = FastAPI(root_path=config('REVERSE_PROXY_ROOT_PATH'))
app.include_router(user_routes.router)


@app.get('/healthcheck')
def healthcheck():
    return f'I am ok {datetime.datetime.now()}'


if __name__ == '__main__':
    users_models.Base.metadata.create_all(bind=engine)
    uvicorn.run("main:app", host='0.0.0.0', port=8000, reload=True)
