import os

from dotenv import load_dotenv
from libsql_client import create_client
from fastapi import FastAPI, HTTPException, status
import Models



app = FastAPI()
load_dotenv()


URL_TURSO=os.environ.get("TURSO_DATABASE_URL")
TOKEN=os.environ.get("TURSO_AUTH_TOKEN")



def db_cliente():
 cliente= create_client(URL_TURSO,auth_token=TOKEN)
 return cliente



     