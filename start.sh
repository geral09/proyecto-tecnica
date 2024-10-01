#!/bin/sh
# Asegúrate de que el script sea ejecutable
# chmod +x start.sh

# Iniciar la aplicación con gunicorn
gunicorn main:app --bind 0.0.0.0:$PORT
