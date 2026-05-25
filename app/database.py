import sqlite3

def get_connection():
    """Função para obter uma conexão com o banco de dados SQLite."""
    return sqlite3.connect("clima.db")