import os
import psycopg

from dotenv import load_dotenv

#carrega as variáveis de ambiente do arquivo .env
load_dotenv()

def get_connection():
    """Função para obter uma conexão com o banco de dados PostgreSQL."""
    
    return psycopg.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        client_encoding="utf-8"
    )