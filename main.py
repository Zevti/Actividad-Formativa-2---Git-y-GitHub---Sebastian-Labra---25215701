import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QWidget


class Principal(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.inicializar_gui()

    def inicializar_gui(self) -> None:
        self.setWindowTitle('Ventana Principal')
        self.setGeometry(560, 290, 800, 500)

        self.generar_widgets()
        self.generar_botones()
        self.generar_layout()
        self.conectar_botones()

        self.show()

    # Con cariño profe, andaba aburrido
    def generar_widgets(self) -> None:
        self.saludo = QLabel('Hola profe o ayudantes', self)
        self.saludo.resize(self.saludo.sizeHint())

        self.cobreloa = QLabel('Imagine estar en segunda... Cobreloa', self)
    
    def generar_botones(self) -> None:
        self.salir = QPushButton('Salir del programa', self)
        self.salir.resize(self.salir.sizeHint())

    def generar_layout(self) -> None:
        layout = QVBoxLayout()
        layout.addWidget(self.saludo)
        layout.addWidget(self.cobreloa)
        layout.addWidget(self.salir)

        layout_principal = QHBoxLayout()
        layout_principal.addStretch()
        layout_principal.addLayout(layout)
        layout_principal.addStretch()

        self.setLayout(layout_principal)

    def conectar_botones(self):
        self.salir.clicked.connect(QCoreApplication.instance().quit)


def hook(type, value, traceback) -> None:
    print(type)
    print(traceback)


sys.__excepthook__ = hook

app = QApplication([])
ventana = Principal()

sys.exit(app.exec())