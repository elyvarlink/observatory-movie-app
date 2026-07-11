from fastapi import FastAPI
from .routers import movie_id, list_movies, user_action


app = FastAPI()

# Include the routers for the different endpoints. This will allow us to separate the different endpoints into different files, making it easier to manage and maintain the code.
app.include_router(list_movies.router)
app.include_router(movie_id.router)
# app.include_router(user_action.router)



# The beginning of the API, welcoming the user to the API and providing a message.
@app.get("/")
async def root():
    return {"message": "Welcome to the Movie API!"}