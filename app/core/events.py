from fastapi import FastAPI


# from app.databases import database
# from app.databases.events import connect_to_db, close_db_connection


def create_start_app_handler(app: FastAPI):
    async def start_app():
        # await database.connect()
        pass

    return start_app


def create_stop_app_handler(app: FastAPI):
    async def stop_app():
        # await database.disconnect()
        pass

    return stop_app
