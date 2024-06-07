from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/outro_recurso")
def pegar_recurso():
    return "Recuso extra aqui!"

@app.get("/outro_recurso/{id}")
def cria_recuso():
    return {"message": id}