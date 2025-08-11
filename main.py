from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensaje": "¡Hola desde Docker y FastAPI! cambioooos"}

@app.get("/url")
def read_url():
    return {"mensaje": "urljson"}