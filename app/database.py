import psycopg

def get_connection():

    """Função para obter uma conexão com o banco de dados PostgreSQL."""
    return psycopg.connect(
        host="localhost",
        port=5432,
        dbname="clima",
        user="postgres",
        password="junior48",
        client_encoding="utf-8"
    )