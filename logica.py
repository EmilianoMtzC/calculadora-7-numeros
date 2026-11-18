"""Paso 1 - Lógica del programa (sin interfaz gráfica).

Todas las operaciones son funciones puras que reciben una lista de 7 números.
La interfaz (app.py) solo las llama, así se pueden probar por separado.
"""
from math import prod

CANTIDAD_NUMEROS = 7


def validar_numeros(textos):
    """Convierte una lista de textos a float.

    Lanza ValueError con un mensaje claro si falta algún dato o no es número.
    """
    if len(textos) != CANTIDAD_NUMEROS:
        raise ValueError(f"Se requieren exactamente {CANTIDAD_NUMEROS} números.")
    numeros = []
    for i, texto in enumerate(textos, start=1):
        limpio = texto.strip().replace(",", ".")
        if not limpio:
            raise ValueError(f"El número {i} está vacío.")
        try:
            numeros.append(float(limpio))
        except ValueError:
            raise ValueError(f"El número {i} ('{texto}') no es válido.") from None
    return numeros


def formatear(valor):
    """Muestra enteros sin '.0' y decimales con hasta 4 cifras."""
    if valor == int(valor):
        return str(int(valor))
    return f"{valor:.4f}".rstrip("0").rstrip(".")


def suma(numeros):
    return sum(numeros)


def promedio(numeros):
    return sum(numeros) / len(numeros)


def producto(numeros):
    return prod(numeros)


def mayor_y_menor(numeros):
    return max(numeros), min(numeros)


def ordenar_ascendente(numeros):
    return sorted(numeros)


# --- Funciones que devuelven el texto final a mostrar -----------------------

def op_suma(numeros):
    return f"Suma = {formatear(suma(numeros))}"


def op_promedio(numeros):
    return f"Promedio = {formatear(promedio(numeros))}"


def op_producto(numeros):
    return f"Producto = {formatear(producto(numeros))}"


def op_mayor_menor(numeros):
    mayor, menor = mayor_y_menor(numeros)
    return f"Mayor = {formatear(mayor)}\nMenor = {formatear(menor)}"


def op_ordenar(numeros):
    return "Orden ascendente:\n" + ", ".join(formatear(n) for n in ordenar_ascendente(numeros))


# Menú: (etiqueta del botón, función). La interfaz lo recorre para crear botones.
OPERACIONES = [
    ("1. Suma", op_suma),
    ("2. Promedio", op_promedio),
    ("3. Producto", op_producto),
    ("4. Mayor y menor", op_mayor_menor),
    ("5. Ordenar ascendente", op_ordenar),
]


def ejecutar(indice, textos):
    """Valida los textos y ejecuta la operación número `indice` del menú."""
    numeros = validar_numeros(textos)
    return OPERACIONES[indice][1](numeros)
