# FastAPI Project Template

A production-ready FastAPI template with SQLAlchemy, Alembic, and modular architecture.

## Features

- � **Pre-configured FastAPI** with best practices
- 🗄 **SQLAlchemy ORM** with async support
- 📊 **Alembic** for database migrations
- 🧩 **Modular architecture** (core/infrastructure/internal)
- 🔒 **Environment variables** management
- 📜 **Pre-commit hooks** setup

## Project Structure
![Conceptual project structure](assets/images/structure.svg)

## Quick Start

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/fastapi-template.git
   cd fastapi-template
   ```

2. Install dependencies
    ```bash
    uv install
    ```

3. Configure environment:
    ```bash
    cp .env.example .env
    ```
4. Run the application:
    ```bash
    uv run main.py
    ```
5. Open http://localhost:3000/docs to see Swagger UI

## Database Migrations

### Database Migrations

1. Create new migration:
    ```bash
    alembic revision --autogenerate -m "init"
    ```
2. Apply migrations:
    ```bash
    alembic upgrade head
    ```


