#!/bin/bash
source .venv/bin/activate
cd backend_supermercado
python manage.py runserver 0.0.0.0:${PORT:-8000}