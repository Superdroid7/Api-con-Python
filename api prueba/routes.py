from Conexion import db_cliente
import Models
from fastapi import FastAPI, HTTPException, status


app = FastAPI()

@app.post("/user/create/")
async def crear_usuario(user: Models.User):
 
 try:
   cliente=db_cliente()
  

   await    cliente.execute(
        "INSERT INTO users (nombre,correo,edad) VALUES (?,?,?)",
        [user.nombre, user.correo, user.edad]
        )
   await cliente.close()

   return {
     "message": "PIOLA",
     "nombre": user.nombre,
     "correo":user.correo
   }
 
 except Exception as e:
  
  raise HTTPException(
   status_code= status.HTTP_500_INTERNAL_SERVER_ERROR,
   detail=f"Mamawebo la cagaste {e}"
  )
 
@app.get("/user")
async def obtener_usuarios():
  cliente = db_cliente()

  try:
    result = await cliente.execute("SELECT nombre, correo, edad FROM users")
    await cliente.close()

    lista_usuarios=[]

    columns = result.columns

    for row in result.rows:
      user_data = dict(zip(columns, row))
      lista_usuarios.append(user_data)

    return lista_usuarios
  except Exception as e:
 
    raise  HTTPException(
      status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
      detail=f"error en esto estupido: {e}"
    )
  
@app.get("/users/{user_id}")
async def samuel_gay(user_id: int):
  
  cliente = db_cliente()

  try:
    result = await cliente.execute (f"SELECT * FROM users WHERE id = {user_id}")
    await cliente.close()

    lista_usuario= []

    columnas = result.columns

    for row in result.rows:
      user_data = dict(zip(columnas, row))
      lista_usuario.append(user_data)
    
    return lista_usuario
  except Exception as e:
     
    raise HTTPException(
      status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
      detail=f"mamawebo tienes error estupido {e}"
    )
  
@app.put("/users/{user_id}")
async def updateUser(user : Models.User, user_id: int):
  
  cliente = db_cliente()

  try:
    await cliente.execute(
      f"UPDATE users SET nombre=?, correo=?, edad=? WHERE ID = ?", 
      [user.nombre, user.correo, user.edad, user_id]
      )
    cliente.close()

    return{
      "message": "God",
      "nombre": user.nombre,
      "correo": user.correo,
      "edad": user.edad
      }
  
  except Exception as e:
    
    raise HTTPException(
      status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
      detail=f"Hubo en error mamawebo {e}"
    )
  


  
  






      

  
  

  

