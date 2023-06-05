import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from endpoint import *


def create_app() -> FastAPI():
    app = FastAPI()

    origins = ["*"]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=["*"],
        allow_methods=["*"],
        allow_headers=["*"]
    )

    app.include_router(buyer_service)

    return app


app = create_app()




