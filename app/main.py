import uvicorn
from fastapi import FastAPI

from app.configs.settings import get_settings

settings = get_settings()
app = FastAPI(title=settings.APP_NAME)


@app.get("/")
def read_root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run("app.main:app", loop="uvloop", http="httptools", reload=False)
