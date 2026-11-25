"""Punto de entrada WSGI para servidores de producción (Render, Railway, PythonAnywhere)."""
import os
import sys
from pathlib import Path

# Asegurar que el directorio raíz esté en sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent))

from web.app import app

if __name__ == "__main__":
    port = int(os.environ.get("PORT", os.environ.get("MESA_PORT", 5000)))
    app.run(host="0.0.0.0", port=port)
