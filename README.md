# Softfocus - Loss Communication API

## Requirements

-   Python 3.x [see](https://www.python.org/)
-   Poetry [see](https://www.python.org/)
-   Docker [see](https://www.docker.com/)

## Running the project

First is required to run the database, which can be done with Docker or any actual instance of Postgres.

### Database

```sh
docker-compose up --build -d
```

### Poetry Shell

After that run activates the poetry shell.

```sh
poetry shell
```

### Dependencies

Install all deps.

```sh
poetry install
```

### Running Migrations

Change the file `alembic.ini`. Set the variable `sqlalchemy.url` to the actual URL of your database.
Eg: `postgresql://example:example@localhost:5432/example`

```sh
poetry run alembic upgrade heads
```

### Running the API

```sh
uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
```

### Docs

Two types of Documentation are available. One was provided from Redoc and the other from Swagger.

Redoc: `<host>:<port>/redoc`

Swagger:`<host>:<port>/docs`

Have fun.
