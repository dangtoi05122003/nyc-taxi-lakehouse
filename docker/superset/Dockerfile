FROM apache/superset:latest

USER root

RUN /app/.venv/bin/python -m ensurepip --upgrade || true && \
    /app/.venv/bin/python -m pip install --upgrade pip || true && \
    /app/.venv/bin/python -m pip install trino sqlalchemy-trino

USER superset