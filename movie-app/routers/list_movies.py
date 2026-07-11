from fastapi import APIRouter, HTTPException

router = APIRouter()






# This will be a global variable that will hold the movie data. It can be accessed by other routers as well.
# this is temporary data, as we will eventually be using a database to store the movie data. This is just for testing purposes.
movie_data = [
    {"id": 1, "title": "Spirit", "year": 1995},
    {"id": 2, "title": "White Chicks", "year": 1996},
    {"id": 3, "title": "Stuart Little 3", "year": 1997},
    {"id": 4, "title": "Warrior", "year": 1998},
    {"id": 5, "title": "Wine", "year": 1999}
]

#This enpoints returns all the movies in the movie_data list.
@router.get("/movies")
async def get_movies():
    return movie_data


# movie_data = [
#     {"id": 1, "title": "Spirit", "year": 1995},
#     {"id": 2, "title": "White Chicks", "year": 1996},
#     {"id": 3, "title": "Stuart Little 3", "year": 1997},
#     {"id": 4, "title": "Warrior", "year": 1998},
#     {"id": 5, "title": "Wine", "year": 1999}
# ]


# async def movies_data():
#     movie_1  = {"id": 1,
#                 "title": "Spirit",
#                 "year": 1995
#     }
#     movie_2  = {"id": 2,
#                 "title": "White Chicks",
#                 "year": 1996
#     }
#     movie_3  = {"id": 3,
#                 "title": "Stuart Little 3",
#                 "year": 1997
#     }
#     movie_4  = {"id": 4,
#                 "title": "Warrior",
#                 "year": 1998
#     }
#     movie_5  = {"id": 5,
#                 "title": "Wine",
#                 "year": 1999
#     }
    
#     return [movie_1, movie_2, movie_3, movie_4, movie_5]

