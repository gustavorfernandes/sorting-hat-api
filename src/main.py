import uvicorn
from fastapi import FastAPI
from resources import house_router, common_router

app = FastAPI()

app.include_router(common_router, prefix="")
app.include_router(house_router, prefix="/house")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
