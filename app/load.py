from app.logger import logger
from app.database import get_connection

def load_data(data):
    """Função de carga dos dados transformados para o banco de dados"""
    
    logger.info("Iniciando a carga dos dados.")

    conn = None  # Inicializa a variável de conexão para garantir que esteja definida mesmo em caso de erro

    try:
        # Cria conexão com banco de dados SQLite
        conn = get_connection()
        cursor = conn.cursor()

        # Cria tabela se não existir
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS clima (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            temperatura REAL,
            vento REAL,
           data_hora TEXT
        )
        """)

        # Insere os dados transformados na tabela
        cursor.execute(
            """
            INSERT INTO clima (temperatura, vento,data_hora)
            VALUES (?, ?, ?)
            """,
            (data["temperatura"], data["vento"], data["data_hora"]),
        )

        # Salvar e fechar conexão
        conn.commit()

        logger.info("Dados inseridos no banco")

        # Opcionalmente, retornar um status ou o ID do registro inserido
    except Exception as erro:
        logger.error(f"Erro no pipeline: {erro}")

        # Opcionalmente, re-raise a exceção para que ela possa ser tratada em outro lugar ou para interromper o processo
    finally:
        if conn:
            conn.close()
            logger.info("Conexão encerrada")
