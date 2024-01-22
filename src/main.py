from fastapi import FastAPI
from routers import  users
from fastapi.templating import Jinja2Templates

app = FastAPI()

# # Include routers
# app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
# app.include_router(groups.router, prefix="/groups", tags=["Groups"])
app.include_router(users.router, prefix="/users", tags=["Users"])

    

# Initialize the database

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
