# Desafio-backend-seazone
DESAFIO BACKEND DA SEAZONE (APENAS PARA O DESAFIO PROMOVIDO DA EMPRESA SEAZONE)

## Arquitetura de Pastas

app/<br>
├── api/<br>
│    ├── v1/<br>
│          ├── availability.py<br>
│          ├── cancel_reservation.py<br>
│          ├── list_properties.py<br>
│          ├── properties.py<br>
│          └── reservation.py<br>
├── db/<br>
│      ├── database.py<br>
│      ├── models.py<br>
│      └── schemas.py<br>
├── main.py<br>
│<br>
docker/<br>
│      └── docker-compose.yaml<br>
│<br>      
tests/<br>
│      ├── test_availability.py<br>
│      ├── test_create_properties.py<br>
│      └── test_reservation_and_cancel.py<br>
│<br>
.env.exemplo (Duplicar na pasta do Docker!!)<br>
.gitignore<br>
alembic.ini<br>
README.md<br>
requirements.txt<br>

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

OBS: Deverá ter um Docker instalado na máquina para subir o banco de dados PostgreSQL, no arquivo do docker configurei uma visão do banco de dados como se fosse o PGAdmin, as credenciais estão no .env.exemplo).

OPCIONAL: Recomendo criar uma .venv para o projeto, pois o Python pode utilizar o interpretador errado!<br>
`py 3.11 -m venv .venv (Win)` ou `python 3.11 -m venv .venv (MacOS ou Linux)` 

ATIVAR O AMBIENTE VIRTUAL:
`.venv\Scripts\activate (Win)` ou `source .venv/bin/activate (MacOS ou Linux)`

ATIVAR O DOCKER:
Utilizar o comando - `docker compose up` (Dentro da pasta do Docker no projeto), essa aplicação sobe o banco de dados (Lembrando que o .env.exemplo deve ser duplicado para essa pasta também, é importante já que o docker não está na raiz do projeto).

ATIVAR OS SERVIÇOS WEB:
Para subir o web utilize `uvicorn app.main:app --reload` (Geralmente o Swagger vai estar na porta 8000 | http://localhost:8000/docs)

INSTALAR OS REQUIREMENTS DO PYTHON:  
Deixei um arquivo .txt para os requirements do Python, para utilizar basta digitar no terminal `pip install -r requirements.txt` (Isso é importante, porque o Python pode ter versões diferentes dependendo de quando for instalar)

COMANDO PARA UTILIZAR O PYTEST (APENAS WINDOWS):
Para rodar os testes automatizados vai ter que utilizar o comando que deixei logo abaixo, porque ele está dentro de uma pasta tests e não na raiz do projeto:<br>
`$env:PYTHONPATH = "$PWD"                                                                                      
pytest tests/`          
