
```
pip install fastapi

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/outro_recurso")
async def pegar_recurso():
    return "Recuso extra aqui!"
```
pip install uvicorn[standard]

uvicorn exemplo_003:app