from app.logger import logger

def transform_weather(api_data):
    """Função de transformação de dados do clima."""
    logger.info("Iniciando a transformação dos dados.")
    
    weather = api_data["current_weather"] # Extrai os dados do clima atual do dicionário retornado pela API
    
    logger.info(f"Dados do clima extraídos: {weather}") # Loga os dados extraídos para facilitar a depuração em caso de erros

    return {
        "temperatura": weather["temperature"], # Extrai a temperatura
        "vento": weather["windspeed"], # Extrai a velocidade do vento
        "data_hora": weather["time"] # Extrai a hora do registro do clima
    }