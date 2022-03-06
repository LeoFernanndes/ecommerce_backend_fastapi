import datetime
import uvicorn
from fastapi import FastAPI
from users import models as users_models
from database_connections.mysql_database_connection import engine
from users import routes as user_routes


app = FastAPI(root_path='/api')
app.include_router(user_routes.router)


@app.get('/healthcheck')
def healthcheck():
    return f'I am ok {datetime.datetime.now()}'


if __name__ == '__main__':
    users_models.Base.metadata.create_all(bind=engine)
    uvicorn.run(app, host='0.0.0.0', port=8000)
