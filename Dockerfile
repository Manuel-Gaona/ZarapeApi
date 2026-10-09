# Imagen de producción de la API de El Zarape
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    FLASK_APP=run.py \
    FLASK_DEBUG=0

WORKDIR /app

# Las dependencias se instalan primero: si no cambian, Docker reutiliza esta capa
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# La app corre con un usuario sin privilegios. Las carpetas de datos se crean
# aquí para que los volúmenes hereden sus permisos.
RUN useradd --create-home zarape \
    && mkdir -p instance uploads \
    && chown -R zarape:zarape /app
USER zarape

EXPOSE 5000

# Swarm usa esta comprobación para saber si el contenedor está sano
HEALTHCHECK --interval=30s --timeout=5s --start-period=30s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:5000/api/salud', timeout=3)"

CMD ["sh", "docker-entrypoint.sh"]
