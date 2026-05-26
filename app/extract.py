import requests
from app.logger import logger

def extract_weather():
    """Função de extração dos dados do clima"""
    # URL da API de clima
    url = "https://api.open-meteo.com/v1/forecast?latitude=-21.47&longitude=-47.00&current_weather=true"
    
    logger.info("Iniciando a extração dos dados.")
    
    response = requests.get(url, timeout=10) # Realiza a requisição GET para a API com um timeout de 10 segundos para evitar que o processo fique travado indefinidamente
    response.raise_for_status() # Verifica se a requisição foi bem-sucedida, caso contrário, lança uma exceção
    
    logger.info(f"Resposta da API: {response.text}") # Loga a resposta da API para facilitar a depuração em caso de erros

    return response.json() # Retorna os dados da API em formato JSON, que será processado na etapa de transformação