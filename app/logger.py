import logging
import os

# Cria o diretório de logs, se não existir
os.makedirs("logs", exist_ok=True)

"""Configuração do sistema de logs"""
logging.basicConfig(
    level=logging.INFO,
    filename="logs/pipeline.log",
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

logger = logging.getLogger(__name__)