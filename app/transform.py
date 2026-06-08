from app.logger import logger

def transform_weather(api_data):
    """Função de transformação de dados do clima."""
    logger.info("Iniciando a transformação dos dados.")
    
    if "current_weather" not in api_data: # Verifica se os dados de clima atual estão presentes na resposta da API
        raise ValueError("Dados de clima atual não encontrados na resposta da API.")
    
    weather = api_data["current_weather"] # Extrai os dados do clima atual do dicionário retornado pela API
    
    campos_obrigatorios = [
        "temperature",
        "windspeed", 
        "time"] # Define os campos obrigatórios que devem estar presentes nos dados do clima
    
    for campo in campos_obrigatorios:
        if campo not in weather: # Verifica se cada campo obrigatório está presente nos dados do clima
            raise ValueError(f"Campo '{campo}' ausente nos dados do clima.") # Lança um erro se algum campo obrigatório estiver ausente

    if weather["temperature"] is None:
        raise ValueError("Temperatura veio nula.")
    
    if weather["windspeed"] is None:
        raise ValueError("Velocidade do vento veio nula.")
    
    if weather["time"] is None:
        raise ValueError("Data e hora veio nulas.")
    
    logger.info(f"Dados do clima extraídos: {weather}") # Loga os dados extraídos para facilitar a depuração em caso de erros

    return {
        "temperatura": weather["temperature"], # Extrai a temperatura
        "vento": weather["windspeed"], # Extrai a velocidade do vento
        "data_hora": weather["time"] # Extrai a hora do registro do clima
    }