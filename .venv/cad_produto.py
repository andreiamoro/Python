from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit
import sys

class CadastroProduto(QWidget):
    # Método init para inicializar a nossa janela
    def __init__(self):
        super().__init__()
        # Vamos setar um texto para o título da janela
        self.setWindowTitle("Cadastro de Produtos")
        # Setar a posição e o tamanho da janela
        self.setGeometry(750,250,300,450)

        self.setStyleSheet("background-color:#64b5f6")

        self.nome_label = QLabel("Nome do Produto")
        # Vamos aplicar uma formatação na label usando
        # comandos de CSS(Cascade Style Sheet - Folha de Estilo em Cascata)
        self.nome_label.setStyleSheet("QLabel{font-size:20pt;color:#5e35b1;font-weight:bold}")
        self.nome_edit = QLineEdit()
        self.nome_edit.setStyleSheet("QLineEdit{border-radius:10px; background-color:#dddddd; font-size:20pt;color:#330000}")

        self.tipo_label = QLabel("Tipo")
        self.tipo_label.setStyleSheet("QLabel{font-size:20pt;color:#5e35b1;font-weight:bold}")
        self.tipo_edit = QLineEdit()
        self.tipo_edit.setStyleSheet("QLineEdit{border-radius:10px;background-color:#dddddd;font-size:20pt;color:#330000}")

        self.preco_label = QLabel("Preço")
        self.preco_label.setStyleSheet("QLabel{font-size:20pt;color:#5e35b1;font-weight:bold}")
        self.preco_edit = QLineEdit()
        self.preco_edit.setStyleSheet("QLineEdit{border-radius:10px;background-color:#dddddd;font-size:20pt;color:#330000}")

        self.cadastrar_button = QPushButton("Cadastrar")
        self.cadastrar_button.setStyleSheet("QPushButton{background-color:#330033;color:#ffffff; font-size:20pt}")

        self.layout_vertical = QVBoxLayout()
        # adicionar os controles no layout
        self.layout_vertical.addWidget(self.nome_label)
        self.layout_vertical.addWidget(self.nome_edit)

        self.layout_vertical.addWidget(self.tipo_label)
        self.layout_vertical.addWidget(self.tipo_edit)

        self.layout_vertical.addWidget(self.preco_label)
        self.layout_vertical.addWidget(self.preco_edit)

        self.layout_vertical.addWidget(self.cadastrar_button)

        # Adicionar o layout veritcal com todos os controles a nossa janela
        self.setLayout(self.layout_vertical)

# Apresentar a janela
app = QApplication(sys.argv)
cad = CadastroProduto()
cad.show()
app.exec()
