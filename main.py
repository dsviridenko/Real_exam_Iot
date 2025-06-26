from fastapi import FastAPI

from app.api.v1.web import router as web_router

app = FastAPI(title="My API")

# Все ваши веб-роуты в одном месте
app.include_router(web_router)