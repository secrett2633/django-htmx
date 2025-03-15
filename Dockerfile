# Python 3.11.11 이미지를 기반으로 빌드 환경을 설정
FROM python:3.11.11 AS builder

# poetry 버전 설정 (기본값: 1.5.1)
ARG POETRY_VERSION=1.5.1

# poetry 설치
RUN python -m pip install --no-cache-dir poetry==${POETRY_VERSION}

# 환경 변수 설정
ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# 작업 디렉토리 설정
WORKDIR /workdir

# poetry 의존성 파일 복사 및 의존성 설치
COPY pyproject.toml poetry.lock /workdir/
RUN poetry install --no-root && rm -rf $POETRY_CACHE_DIR  # 의존성 설치 후 캐시 삭제

# 애플리케이션 코드 복사
COPY /mytodo /workdir/mytodo
COPY .env /workdir/.env
