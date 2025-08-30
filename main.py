from fastapi import FastAPI
from routers import auth

app = FastAPI()
app.include_router(auth.router)




@app.get("/")
def read_root():
    return {"mensaje": "¡Hola desde Docker y FastAPI! cambioooos"}

@app.get("/url")
def read_url():
    return {"mensaje": "urljson"}
