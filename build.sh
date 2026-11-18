#!/bin/bash
# Paso 3 - Empaquetado (Linux/macOS; en Windows usar build.bat)
pip install -r requirements.txt
pyinstaller --noconfirm --clean --windowed --name Calculadora7 --add-data "styles.qss:." --add-data "fuentes:fuentes" app.py
