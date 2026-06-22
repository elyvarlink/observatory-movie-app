
from typing import Annotated
from fastapi import FastAPI, HTTPException, Path
app = FastAPI()

movie_1  = {"id": 1,
            "title": "Spirit",
            "year": 1995
}
movie_2  = {"id": 2,
            "title": "White Chicks",
            "year": 1996
}
movie_3  = {"id": 3,
            "title": "Stuart Little 3",
            "year": 1997
}
movie_4  = {"id": 4,
            "title": "Woke",
            "year": 1998
}
movie_5  = {"id": 5,
            "title": "Wine",
            "year": 1999
}

# the health of the program
@app.get("/health")
async def root():
    return {"status": "ok"}

#movie data
@app.get("/movies")
async def movies_data():
    return [movie_1, movie_2, movie_3, movie_4, movie_5]



#returns a single movie by its id.
@app.get("/movies/{movie_id}")
async def single_movie_by_id(movie_id: int):
    if movie_id not in [movie_1["id"], movie_2["id"], movie_3["id"], movie_4["id"], movie_5["id"]]:
        raise HTTPException(status_code=404, detail="Movie not found")
    return {movie_id: [movie_1, movie_2, movie_3, movie_4, movie_5][movie_id-1]}





