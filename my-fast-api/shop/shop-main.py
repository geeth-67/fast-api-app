from fastapi import FastAPI
from user_router import router as user_router
from product_router import router as product_router

app = FastAPI()

app.include_router(router=user_router)
app.include_router(router=product_router)
