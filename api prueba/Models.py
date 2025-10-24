from pydantic import BaseModel


class User(BaseModel):
    nombre:str
    correo:str
    edad:int