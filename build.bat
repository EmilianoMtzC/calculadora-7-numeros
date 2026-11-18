@echo off
REM Paso 3 - Empaquetado (ejecutar en Windows)
pip install -r requirements.txt
pyinstaller --noconfirm --clean --windowed --name Calculadora7 --add-data "styles.qss;." --add-data "fuentes;fuentes" app.py
echo.
echo Listo: dist\Calculadora7\Calculadora7.exe
