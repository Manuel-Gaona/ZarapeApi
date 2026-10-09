#!/bin/sh
# Arranque del contenedor: prepara la base de datos y enciende el servidor.
set -e

# Aplica las migraciones pendientes (no hace nada si ya está al día)
flask db upgrade

# Carga los datos de ejemplo solo si se pide y la base está vacía
if [ "${SEED_ON_START:-false}" = "true" ]; then
    flask seed
fi

# gunicorn es el servidor de producción ("flask run" es solo para desarrollo)
exec gunicorn \
    --bind 0.0.0.0:5000 \
    --workers "${GUNICORN_WORKERS:-2}" \
    --access-logfile - \
    run:app
