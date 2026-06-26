from fastapi import FastAPI
from .routers import movie_id, list_movies, user_action


app = FastAPI()


app.include_router(list_movies.router)
app.include_router(movie_id.router)
# app.include_router(user_action.router)




@app.get("/")
async def root():
    return {"message": "Welcome to the Movie API!"}