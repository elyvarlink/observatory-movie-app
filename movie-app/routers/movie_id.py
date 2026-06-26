from fastapi import APIRouter, HTTPException
from .list_movies import movie_data

router = APIRouter()


@router.get("/movies/{movie_id}")
async def single_movie_by_id(movie_id: int):
    if movie_id not in [movie_data[0]["id"], movie_data[1]["id"], movie_data[2]["id"], movie_data[3]["id"], movie_data[4]["id"]]:
        raise HTTPException(status_code=404, detail="Movie not found")
    return {movie_id: [movie_data[0], movie_data[1], movie_data[2], movie_data[3], movie_data[4]][movie_id-1]}