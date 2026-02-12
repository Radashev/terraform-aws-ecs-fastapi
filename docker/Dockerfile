FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir poetry

# Copy dependency files first for caching
COPY pyproject.toml poetry.lock* /app/

# Install dependencies only (no project install)
RUN poetry install --no-root --no-interaction

# Copy app code
COPY app/ /app/app

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
