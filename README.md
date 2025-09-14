# Desafio-backend-seazone
DESAFIO BACKEND DA SEAZONE (APENAS PARA O DESAFIO PROMOVIDO PARA A EMPRESA SEAZONE)

## Arquitetura de Pastas


## Endpoints Principais:

- **POST /api/v1/properties/**  
  Cria uma nova propriedade.

- **POST /api/v1/reservation/**  
  Cria uma nova reserva para a propriedade.
  
- **GET /api/v1/properties/availability**  
  Verifica disponibilidade de uma propriedade em determinadas datas.

- **DELETE /api/v1/reservation/{reservation_id}**  
  Cancela uma reserva pelo ID.

- **GET /api/v1/list_reservations/**  
  Lista reservas por propriedade ou email do cliente.

- **GET /api/v1/list_properties/**  
  Lista todas as propriedades caso selecione True no `list_all` ou pode aplicar filtros (bairro, cidade, estado, capacidade ou preço máximo).


## Tecnologias:
- Python 3.11.7
- SQLAlchemy
- Alembic
- FastAPI
- PostgreSQL
- Docker
- Pytest

## Como utilizar da melhor forma (Deixei esse campo para facilitar o uso da API):

OBS: Deverá ter um Docker instalado caso não possua para subir o banco de dados PostgreSQL, no arquivo do docker configurei uma visão do banco de dados como se fosse o PGAdmin, as credenciais estão no .env.exemplo).

Utilizar o comando - docker compose up (Dentro da pasta do Docker no projeto), essa aplicação sobe o banco de dados.

Para subir o web utilize uvicorn app.main:app --reload (Geralmente o Swagger vai estar na porta 8000 | http://localhost:8000/docs)

Deixei um arquivo .txt para os requirements do Python, para utilizar basta digitar no terminal `pip install -r requirements.txt` (Isso é importante, porque o Python pode ter versões diferentes dependendo de quando for instalar)

Para rodar os testes automatizados vai ter que utilizar o comando que deixei logo abaixo, porque ele está dentro de uma pasta tests e não na raiz do projeto:
$env:PYTHONPATH = "$PWD"                                                                                      
pytest tests/             
