from fastapi import FastAPI
from . import controllers, database

app = FastAPI()

# Iniciar la base de datos
database.init_db()

# Incluir rutas
app.include_router(controllers.router)
