from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout
)
 
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt
from sys import argv
 
 
class TelaPrincipal(QWidget):
 
    def __init__(self):
        super().__init__()
 
        self.setWindowTitle("Seja Voluntário")
        self.resize(1000, 500)
 
        self.setWindowIcon(QIcon("luna.jpg"))
 
        # Layout principal
        layout_principal = QHBoxLayout()
 
        # =====================
        # COLUNA ESQUERDA
        # =====================
 
        lado_esquerdo = QVBoxLayout()
 
        imagem = QLabel()
 
        pixmap = QPixmap("luna.jpg")
 
        imagem.setPixmap(
            pixmap.scaled(
                500,
                500,
                Qt.AspectRatioMode.KeepAspectRatio
            )
        )
 
        imagem.setAlignment(Qt.AlignmentFlag.AlignCenter)
 
        lado_esquerdo.addWidget(imagem)
 
        # =====================
        # COLUNA DIREITA
        # =====================
 
        lado_direito = QVBoxLayout()
 
        titulo = QLabel("Seja Voluntário.")
        titulo.setStyleSheet("""
            font-size: 24px;
            color: orange;
            font-weight: bold;
        """)
 
        subtitulo = QLabel(
            "Ajude um aumigo a encontrar um lar!"
        )
 
        subtitulo.setStyleSheet("""
            font-size: 14px;
            color: gray;
        """)
 
        nome = QLineEdit()
        nome.setPlaceholderText("Digite seu nome")
 
        email = QLineEdit()
        email.setPlaceholderText("Digite seu email")
 
        senha = QLineEdit()
        senha.setPlaceholderText("Digite sua senha")

        botao = QPushButton("Cadastrar")
        botao_facebook = QPushButton("")
        botao_facebook.setIcon(QIcon("iconf.png"))

        botao_google = QPushButton("")
        botao_google.setIcon(QIcon("icong.png"))
  

        botao.setStyleSheet("""
            background-color: orange;
            color: white;
            padding: 10px;
            font-weight: bold;
        """)
 
        lado_direito.addWidget(titulo)
        lado_direito.addWidget(subtitulo)
        lado_direito.addSpacing(20)
 
        lado_direito.addWidget(nome)
        lado_direito.addWidget(email)
        lado_direito.addWidget(senha)
 
        lado_direito.addSpacing(10)
 
        lado_direito.addWidget(botao)
        lado_direito.addWidget(botao_facebook)
        lado_direito.addWidget(botao_google)
 
        lado_direito.addStretch()
 
        # =====================
        # JUNTA AS COLUNAS
        # =====================
 
        layout_principal.addLayout(lado_esquerdo)
        layout_principal.addLayout(lado_direito)
 
        self.setLayout(layout_principal)
 
 
app = QApplication(argv)
 
tela = TelaPrincipal()
tela.show()
 
app.exec()