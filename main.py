from fastapi import FastAPI
from app.infrastructure.config import get_settings
from app.interfaces.api import setup_routes

def create_app() -> FastAPI:
    app = FastAPI(
        #title=get_settings().APP_NAME,
        #description=get_settings().APP_DESCRIPTION,
        #version=get_settings().APP_VERSION
    )
    
    setup_routes(app)
    
    return app

app = create_app()