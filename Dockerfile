# syntax=docker/dockerfile:1.6
FROM python:3.12-slim AS runtime

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PYTHONPATH=/app/src

WORKDIR /app

COPY requirements.txt requirements-dev.txt ./

ARG INSTALL_DEV="true"
RUN pip install --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt \
 && if [ "$INSTALL_DEV" = "true" ]; then pip install --no-cache-dir -r requirements-dev.txt; fi

COPY pyproject.toml README.md ./
COPY src ./src
COPY tests ./tests

EXPOSE 8000

CMD ["uvicorn", "office_sign.api:create_app", "--factory", "--host", "0.0.0.0", "--port", "8000"]
