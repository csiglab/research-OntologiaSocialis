FROM python:3.12-slim
WORKDIR /srv
COPY bin/ bin/
COPY docs/ docs/
ENV PYTHONUNBUFFERED=1
EXPOSE 8000
CMD ["sh", "-c", "python bin/sync.py --docs-root /srv/docs --port \"${PORT:-8000}\""]
