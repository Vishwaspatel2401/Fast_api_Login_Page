from fastapi import FastAPI
from container import Container
from routers import  users
from dotenv import load_dotenv

load_dotenv('.env')

def create_app():
    container = Container()

    app = FastAPI()
    app.container = container
    app.include_router(users.router)
    return app

app = create_app()

# # Include routers
# app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
# app.include_router(groups.router, prefix="/groups", tags=["Groups"])
app.include_router(users.router, prefix="/users", tags=["Users"])

    

# Initialize the database

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
