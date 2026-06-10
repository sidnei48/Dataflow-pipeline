Este projeto tem como objetivo demonstrar conceitos fundamentais de Engenharia de Dados através da construção de uma pipeline ETL completa.

A aplicação realiza:

Extração de dados climáticos em tempo real através da API Open-Meteo
Transformação e validação dos dados recebidos
Carga dos dados em banco PostgreSQL
Registro detalhado de logs da execução
Controle de duplicidade dos registros

Arquitetura:
API Open-Meteo -> Extract -> Transform -> Validate -> Load -> PostgreSQL

Tecnologias Utilizadas:
Python 3.11
PostgreSQL 18
Psycopg 3
Requests
Logging
Git e GitHub
