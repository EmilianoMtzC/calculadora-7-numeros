"""Paso 2 - Interfaz gráfica (PyQt6). El estilo vive en styles.qss."""
import sys
from pathlib import Path
from string import Template

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QFont, QFontDatabase
from PyQt6.QtWidgets import (
    QApplication, QDialog, QGraphicsDropShadowEffect, QGridLayout, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QFrame,
)

import logica


def ruta_recurso(nombre):
    """Ruta válida tanto en desarrollo como dentro del .exe de PyInstaller."""
    base = Path(getattr(sys, "_MEIPASS", Path(__file__).parent))
    return base / nombre


TEMAS = {
    "claro": dict(
        fondo="#f8f9fa", superficie="#ffffff", borde="#dadce0",
        texto="#202124", secundario="#5f6368", primario="#1a73e8",
        tonal="#e8f0fe", tonal_hover="#d2e3fc", tonal_press="#aecbfa",
        tonal_texto="#1967d2", hover_neutro="#f1f3f4", press_neutro="#e8eaed",
    ),
    "oscuro": dict(
        fondo="#202124", superficie="#292a2d", borde="#3c4043",
        texto="#e8eaed", secundario="#9aa0a6", primario="#8ab4f8",
        tonal="#2d3b55", tonal_hover="#374a6b", tonal_press="#42587f",
        tonal_texto="#8ab4f8", hover_neutro="#35363a", press_neutro="#3c4043",
    ),
}


def tema_del_sistema(app):
    """'oscuro' si el sistema usa tema oscuro, 'claro' en otro caso."""
    esquema = app.styleHints().colorScheme()
    return "oscuro" if esquema == Qt.ColorScheme.Dark else "claro"


def aplicar_tema(app):
    hoja = ruta_recurso("styles.qss")
    if hoja.exists():
        plantilla = Template(hoja.read_text(encoding="utf-8"))
        app.setStyleSheet(plantilla.substitute(TEMAS[tema_del_sistema(app)]))


def cargar_fuente(app):
    """Registra Google Sans (incluida en fuentes/) y la usa como fuente base."""
    ruta = ruta_recurso("fuentes/GoogleSans.ttf")
    if not ruta.exists():
        return
    ident = QFontDatabase.addApplicationFont(str(ruta))
    familias = QFontDatabase.applicationFontFamilies(ident)
    if familias:
        app.setFont(QFont(familias[0], 10))


class DialogoError(QDialog):
    """Diálogo de error estilo Material: título, mensaje y acción de texto."""

    def __init__(self, padre, titulo, mensaje):
        super().__init__(padre)
        self.setWindowTitle(titulo)
        self.setModal(True)
        # Sin marco del sistema: la tarjeta redondeada con sombra es el diálogo.
        self.setWindowFlags(Qt.WindowType.Dialog | Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        exterior = QVBoxLayout(self)
        exterior.setContentsMargins(20, 20, 20, 24)  # espacio para la sombra
        marco = QFrame()
        marco.setObjectName("dialogo")
        marco.setMinimumWidth(360)
        marco.setMaximumWidth(440)
        sombra = QGraphicsDropShadowEffect(marco)
        sombra.setBlurRadius(32)
        sombra.setOffset(0, 6)
        sombra.setColor(QColor(0, 0, 0, 90))
        marco.setGraphicsEffect(sombra)
        exterior.addWidget(marco)

        caja = QVBoxLayout(marco)
        caja.setContentsMargins(28, 28, 20, 20)
        caja.setSpacing(12)

        cabecera = QLabel(titulo)
        cabecera.setObjectName("dialogo_titulo")
        caja.addWidget(cabecera)

        cuerpo = QLabel(mensaje)
        cuerpo.setObjectName("dialogo_mensaje")
        cuerpo.setWordWrap(True)
        caja.addWidget(cuerpo)

        caja.addSpacing(8)
        acciones = QHBoxLayout()
        acciones.addStretch()
        aceptar = QPushButton("Aceptar")
        aceptar.setObjectName("aceptar")
        aceptar.setCursor(Qt.CursorShape.PointingHandCursor)
        aceptar.setDefault(True)
        aceptar.clicked.connect(self.accept)
        acciones.addWidget(aceptar)
        caja.addLayout(acciones)


class Ventana(QWidget):
    MENSAJE_INICIAL = "Captura los 7 números y elige una operación."

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora de 7 números")
        self.setMinimumWidth(620)
        self.campos = []
        self._construir()

    @staticmethod
    def _tarjeta():
        marco = QFrame()
        marco.setObjectName("tarjeta")
        return marco

    def _construir(self):
        raiz = QVBoxLayout(self)
        raiz.setContentsMargins(32, 28, 32, 28)
        raiz.setSpacing(20)

        titulo = QLabel("Calculadora de 7 números")
        titulo.setObjectName("titulo")
        raiz.addWidget(titulo)

        cuerpo = QHBoxLayout()
        cuerpo.setSpacing(20)
        raiz.addLayout(cuerpo)

        # Tarjeta izquierda: entradas
        tarjeta_entradas = self._tarjeta()
        entradas = QGridLayout(tarjeta_entradas)
        entradas.setContentsMargins(24, 20, 24, 24)
        entradas.setHorizontalSpacing(16)
        entradas.setVerticalSpacing(10)
        encabezado = QLabel("NÚMEROS")
        encabezado.setObjectName("seccion")
        entradas.addWidget(encabezado, 0, 0, 1, 2)
        for i in range(logica.CANTIDAD_NUMEROS):
            etiqueta = QLabel(f"Número {i + 1}")
            etiqueta.setObjectName("descripcion")
            campo = QLineEdit()
            campo.setPlaceholderText("0")
            self.campos.append(campo)
            entradas.addWidget(etiqueta, i + 1, 0)
            entradas.addWidget(campo, i + 1, 1)
        cuerpo.addWidget(tarjeta_entradas, 3)

        # Tarjeta derecha: operaciones
        tarjeta_menu = self._tarjeta()
        menu = QVBoxLayout(tarjeta_menu)
        menu.setContentsMargins(24, 20, 24, 24)
        menu.setSpacing(8)
        etiqueta_menu = QLabel("OPERACIONES")
        etiqueta_menu.setObjectName("seccion")
        menu.addWidget(etiqueta_menu)
        for i, (texto, _) in enumerate(logica.OPERACIONES):
            # "1. Suma" -> "Suma" (la numeración sobra en una interfaz gráfica)
            boton = QPushButton(texto.split(". ", 1)[-1])
            boton.setCursor(Qt.CursorShape.PointingHandCursor)
            boton.clicked.connect(lambda _=False, n=i: self.operar(n))
            menu.addWidget(boton)
        menu.addStretch()
        limpiar = QPushButton("Limpiar")
        limpiar.setObjectName("limpiar")
        limpiar.setCursor(Qt.CursorShape.PointingHandCursor)
        limpiar.clicked.connect(self.limpiar)
        menu.addWidget(limpiar)
        cuerpo.addWidget(tarjeta_menu, 2)

        # Tarjeta de resultado
        tarjeta_resultado = self._tarjeta()
        caja = QVBoxLayout(tarjeta_resultado)
        caja.setContentsMargins(24, 20, 24, 20)
        caja.setSpacing(6)
        etiqueta_res = QLabel("RESULTADO")
        etiqueta_res.setObjectName("seccion")
        caja.addWidget(etiqueta_res)
        self.resultado = QLabel()
        self.resultado.setObjectName("resultado")
        self.resultado.setWordWrap(True)
        self.resultado.setMinimumHeight(56)
        self.resultado.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        caja.addWidget(self.resultado)
        raiz.addWidget(tarjeta_resultado)

        self._mostrar(self.MENSAJE_INICIAL, vacio=True)

    def _mostrar(self, texto, vacio=False):
        self.resultado.setText(texto)
        self.resultado.setProperty("vacio", "true" if vacio else "false")
        self.resultado.style().unpolish(self.resultado)
        self.resultado.style().polish(self.resultado)

    def operar(self, indice):
        try:
            texto = logica.ejecutar(indice, [c.text() for c in self.campos])
        except ValueError as error:
            DialogoError(self, "Dato inválido", str(error)).exec()
            return
        self._mostrar(texto)

    def limpiar(self):
        for c in self.campos:
            c.clear()
        self._mostrar(self.MENSAJE_INICIAL, vacio=True)
        self.campos[0].setFocus()


def main():
    app = QApplication(sys.argv)
    cargar_fuente(app)
    aplicar_tema(app)
    # Si el usuario cambia el tema del sistema con la app abierta, se actualiza.
    app.styleHints().colorSchemeChanged.connect(lambda _: aplicar_tema(app))
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
