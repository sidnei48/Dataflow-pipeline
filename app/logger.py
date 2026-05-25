import logging

"""Configuração do sistema de logs"""
logging.basicConfig(
    level=logging.INFO,
    filename="logs/pipeline.log",
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)