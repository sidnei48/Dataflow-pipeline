
def transform_weather(api_data):
    """Função de transformação de dados do clima."""
    weather = api_data["current_weather"] # Extrai os dados do clima atual do dicionário retornado pela API

    return {
        "temperatura": weather["temperature"], # Extrai a temperatura
        "vento": weather["windspeed"], # Extrai a velocidade do vento
        "data_hora": weather["time"] # Extrai a hora do registro do clima
    }