# para correr esto tienes que entrar obligatoriamente al entorno virtual

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"hello":"worl"}