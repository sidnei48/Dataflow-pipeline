from app.extract import extract_weather
from app.transform import transform_weather
from app.load import load_data

try:
    # Etapa de extração
    api_data = extract_weather()
    
    # Etapa de transformação
    transformed_data = transform_weather(api_data)
    
    # Etapa de carga
    load_data(transformed_data)

except Exception as erro:
    print(f"Erro no pipeline: {erro}")