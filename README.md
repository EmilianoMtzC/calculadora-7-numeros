# Calculadora de 7 números

Aplicación de escritorio hecha en Python con PyQt6. Recibe siete números y realiza cinco operaciones sobre ellos. La interfaz sigue el diseño de Google (Material Design), con tipografía Google Sans y tema claro u oscuro según el sistema.

## Operaciones

| Botón | Resultado |
|---|---|
| Suma | Suma de los 7 números |
| Promedio | Media aritmética |
| Producto | Multiplicación de los 7 números |
| Mayor y menor | El valor más alto y el más bajo |
| Ordenar ascendente | Los números de menor a mayor |

## Instalación

### Requisitos

- Python 3.10 o superior
- Git (opcional, para clonar el repositorio)

### Pasos

1. Descarga el proyecto:

   ```bash
   git clone https://github.com/EmilianoMtzC/calculadora-7-numeros.git
   cd calculadora-7-numeros
   ```

2. Crea y activa un entorno virtual:

   ```bash
   # Linux / macOS
   python3 -m venv venv
   source venv/bin/activate

   # Windows (PowerShell)
   python -m venv venv
   venv\Scripts\Activate.ps1
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Ejecuta el programa:

   ```bash
   python app.py
   ```

## Cómo usarlo

1. Escribe un número en cada uno de los siete campos. Acepta enteros y decimales, con punto o con coma (`3.5` o `3,5`), y también negativos.
2. Pulsa el botón de la operación que quieras. El resultado aparece en la tarjeta **Resultado**.
3. Pulsa **Limpiar** para vaciar los campos y empezar de nuevo.

Ejemplo con los números 3, 8, 1, 9, 4, 7 y 2:

| Operación | Resultado |
|---|---|
| Suma | `34` |
| Promedio | `4.8571` |
| Producto | `12096` |
| Mayor y menor | `Mayor = 9` y `Menor = 1` |
| Ordenar ascendente | `1, 2, 3, 4, 7, 8, 9` |

### Errores

Si dejas un campo vacío o escribes algo que no es un número, aparece un diálogo **Dato inválido** que indica cuál campo falla. Corrígelo, pulsa **Aceptar** y vuelve a elegir la operación.

## Estructura del proyecto

| Archivo | Función |
|---|---|
| `logica.py` | Validación de datos y operaciones, sin interfaz |
| `app.py` | Ventana, campos, botones y diálogo de error |
| `styles.qss` | Estilos y colores de los temas claro y oscuro |
| `fuentes/` | Tipografía Google Sans y su licencia (OFL) |
| `test_logica.py` | Pruebas automáticas de la lógica |
| `build.sh`, `build.bat` | Generan el ejecutable con PyInstaller |
| `installer/instalador.iss` | Asistente de instalación para Windows (Inno Setup) |

## Pruebas

```bash
pip install pytest
python -m pytest test_logica.py
```

## Generar el ejecutable e instalador (Windows)

1. Ejecuta `build.bat`. Crea `dist\Calculadora7\Calculadora7.exe`.
2. Instala [Inno Setup 6](https://jrsoftware.org/isinfo.php), abre `installer\instalador.iss` y pulsa **Compile**.
3. El instalador queda en `installer\Output\Instalador_Calculadora7.exe`. Su asistente permite elegir la carpeta de instalación y crear un icono en el escritorio.

En Linux y macOS, `build.sh` genera el ejecutable de esa plataforma.
