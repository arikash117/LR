import uvicorn
from fastapi import FastAPI
import wikipedia
from pydantic import BaseModel

wiki_app = FastAPI()


@wiki_app.get("/cities/{city}")
def cities_city_name(city: str, number_sentences: int):
    return "About city " + city + ": " + wikipedia.summary(city, sentences=number_sentences)


class wiki_search(BaseModel):
    object: str = "City"
    results: int = 3


@wiki_app.post("/search_wiki")
async def wikipedia_search(searching: wiki_search):
    return wikipedia.search(searching.object, results=searching.results)