# Используем официальный образ Python 3.13.3 на основе Debian Bookworm
FROM python:3.13.3-slim-bookworm

# Копируем uv из официального образа
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

# Копируем всё приложение
COPY . /app

# Устанавливаем рабочую директорию
WORKDIR /app

# Устанавливаем зависимости с помощью uv
RUN uv sync --frozen --no-cache

# Настраиваем переменную окружения для Python
ENV PYTHONUNBUFFERED=1

# Настраиваем PATH для использования бинарников из виртуального окружения
ENV PATH="/app/.venv/bin:$PATH"

# Открываем порт
EXPOSE 3000

# Запускаем приложение
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3000"]