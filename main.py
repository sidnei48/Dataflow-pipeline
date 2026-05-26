import time

from app.extract import extract_weather
from app.transform import transform_weather
from app.load import load_data
from app.logger import logger

start_time = time.time()

try:
    logger.info("Iniciando o pipeline de ETL.")
    # Etapa de extração
    api_data = extract_weather()
    
    # Etapa de transformação
    transformed_data = transform_weather(api_data)
    
    # Etapa de carga
    load_data(transformed_data)
    logger.info("Pipeline de ETL concluído com sucesso.")

except Exception as erro:
    logger.error(f"Erro no pipeline: {erro}")

end_time = time.time()
logger.info(f"Tempo total de execução: {end_time - start_time:.2f} segundos")