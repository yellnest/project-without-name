import uvicorn
from fastapi import FastAPI
from app.src.users.router import router as user_router
from app.src.songs.router import router as song_router
from app.src.genre.router import router as genre_router
from app.src.artists.router import router as artist_router

app = FastAPI()

app.include_router(user_router)
app.include_router(song_router)
app.include_router(genre_router)
app.include_router(artist_router)
