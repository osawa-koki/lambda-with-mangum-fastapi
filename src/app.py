from fastapi import FastAPI
from mangum import Mangum

from .routers import ping

app = FastAPI()
app.include_router(ping.router)

lambda_handler = Mangum(app)
