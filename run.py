"""Punto de entrada de la API.

Se puede iniciar con `flask run` o con `python run.py`.
"""

from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
