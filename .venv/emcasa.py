from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QScrollArea
)

from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt, QSize

from sys import argv


class MoroFlix(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("MoroFlix")
        self.resize(1600, 900)
        self.setWindowIcon(QIcon("filmes.png"))

        self.setStyleSheet("""
            QWidget{
                background-color:#171D25;
                color:white;
            }
        """)

        estilo_botao = """
            QPushButton{
                background-color:#00A8E1;
                color:white;
                padding:10px;
                border-radius:5px;
                font-weight:bold;
            }

            QPushButton:hover{
                background-color:#33C4FF;
            }
        """

        # =====================
        # TÍTULO
        # =====================

        titulo = QLabel("MoroFlix")
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        titulo.setStyleSheet("""
            color:#00A8E1;
            font-size:60px;
            font-weight:bold;
        """)

        # =====================
        # CATÁLOGO MARVEL
        # =====================

        titulo_marvel = QLabel("MARVEL")
        titulo_marvel.setStyleSheet("""
            font-size:20px;
            font-weight:bold;
        """)

        catalogo_marvel = QHBoxLayout()
        catalogo_marvel.setSpacing(10)

        filmes_marvel = [
            ("vingadores1.jpg", "Vingadores"),
            ("vingadores2.jpg", "Era de Ultron"),
            ("vingadores3.jpg", "Guerra Infinita"),
            ("vingadores4.jpg", "Endgame"),
            ("homemferro.jpg", "Homem de Ferro"),
            ("capitaoamerica.jpg", "Capitão América"),
            ("thor.jpg", "Thor"),
            ("homemaranha.jpg", "Homem-Aranha")
        ]

        for imagem_arquivo, nome_filme in filmes_marvel:

            imagem = QLabel()
            imagem.setPixmap(
                QPixmap(imagem_arquivo).scaled(
                    220,
                    320,
                    Qt.AspectRatioMode.KeepAspectRatio
                )
            )
            imagem.setAlignment(Qt.AlignmentFlag.AlignCenter)

            nome = QLabel(nome_filme)
            nome.setAlignment(Qt.AlignmentFlag.AlignCenter)

            botao = QPushButton(" Assistir")
            botao.setIcon(QIcon("reproduzir.png"))
            botao.setIconSize(QSize(24, 24))
            botao.setStyleSheet(estilo_botao)

            filme = QVBoxLayout()
            filme.addWidget(imagem)
            filme.addWidget(nome)
            filme.addWidget(botao,alignment=Qt.AlignmentFlag.AlignCenter)

            catalogo_marvel.addLayout(filme)

            widget_marvel = QWidget()
            widget_marvel.setLayout(catalogo_marvel)

            scroll_marvel = QScrollArea()
            scroll_marvel.setWidget(widget_marvel)
            scroll_marvel.setWidgetResizable(True)

            scroll_marvel.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAsNeeded
            )

            scroll_marvel.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )

            scroll_marvel.setFixedHeight(450)

        # =====================
        # CATÁLOGO PIXAR
        # =====================

        titulo_pixar = QLabel("PIXAR")
        titulo_pixar.setStyleSheet("""
            font-size:28px;
            font-weight:bold;
        """)

        catalogo_pixar = QHBoxLayout()
        catalogo_pixar.setSpacing(10)

        filmes_pixar = [
            ("toystory1.jpg", "Toy Story"),
            ("nemo.jpg", "Procurando Nemo"),
            ("divertidamente.jpg", "Divertida Mente"),
            ("monstrossa.jpg", "Monstros S.A."),
            ("rato.jpg", "Ratatouille"),
            ("zoo.jpg","Zootopia"), 
            ("up.jpg", "Up - Altas Aventuras"),
            ("carros.jpg", "Carros")
        ]

        for imagem_arquivo, nome_filme in filmes_pixar:

            imagem = QLabel()
            imagem.setPixmap(
                QPixmap(imagem_arquivo).scaled(
                    220,
                    320,
                    Qt.AspectRatioMode.KeepAspectRatio
                )
            )
            imagem.setAlignment(Qt.AlignmentFlag.AlignCenter)

            nome = QLabel(nome_filme)
            nome.setAlignment(Qt.AlignmentFlag.AlignCenter)

            botao = QPushButton(" Assistir")
            botao.setIcon(QIcon("reproduzir.png"))
            botao.setIconSize(QSize(24, 24))
            botao.setStyleSheet(estilo_botao)

            filme = QVBoxLayout()
            filme.addWidget(imagem)
            filme.addWidget(nome)
            filme.addWidget(
                botao,
                alignment=Qt.AlignmentFlag.AlignCenter
            )

            catalogo_pixar.addLayout(filme)

            widget_pixar = QWidget()
        
        widget_pixar.setLayout(catalogo_pixar)

        scroll_pixar = QScrollArea()
        scroll_pixar.setWidget(widget_pixar)
        scroll_pixar.setWidgetResizable(True)

        scroll_pixar.setHorizontalScrollBarPolicy(
        Qt.ScrollBarPolicy.ScrollBarAsNeeded
        )

        scroll_pixar.setVerticalScrollBarPolicy(
         Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        scroll_pixar.setFixedHeight(450)

        #==========================
        #CATÁLOGO STAR WARS
        #==========================

        titulo_star_wars = QLabel("STAR WARS")
        titulo_star_wars.setStyleSheet("""
            font-size:28px;
            font-weight:bold;
        """)

        catalogo_star_wars = QHBoxLayout()
        catalogo_star_wars.setSpacing(10)

        filmes_star_wars = [
            ("starwars1.jpg", "Episódio I - A Ameaça Fantasma"),
            ("starwars2.jpg", "Episódio II - Ataque dos Clones"),
            ("starwars3.jpg", "Episódio III - A Vingança dos Sith"),
            ("starwars4.jpg", "Episódio IV - Uma Nova Esperança"),
            ("starwars5.jpg", "Episódio V - O Império Contra-Ataca"),
            ("starwars6.jpg", "Episódio VI - O Retorno de Jedi"),
            ("starwars7.jpg", "Episódio VII - O Despertar da Força"),
            ("starwars8.jpg", "Episódio VIII - Os Últimos Jedi")
        ]

        for imagem_arquivo, nome_filme in filmes_star_wars:

            imagem = QLabel()
            imagem.setPixmap(
                QPixmap(imagem_arquivo).scaled(
                    220,
                    320,
                    Qt.AspectRatioMode.KeepAspectRatio
                )
            )
            imagem.setAlignment(Qt.AlignmentFlag.AlignCenter)

            nome = QLabel(nome_filme)
            nome.setAlignment(Qt.AlignmentFlag.AlignCenter)

            botao = QPushButton(" Assistir")
            botao.setIcon(QIcon("reproduzir.png"))
            botao.setIconSize(QSize(24, 24))
            botao.setStyleSheet(estilo_botao)

            filme = QVBoxLayout()
            filme.addWidget(imagem)
            filme.addWidget(nome)
            filme.addWidget(
                botao,
                alignment=Qt.AlignmentFlag.AlignCenter
            )

            catalogo_star_wars.addLayout(filme)

            widget_star_wars = QWidget()
        
        widget_star_wars.setLayout(catalogo_star_wars)

        scroll_star_wars = QScrollArea()
        scroll_star_wars.setWidget(widget_star_wars)
        scroll_star_wars.setWidgetResizable(True)

        scroll_star_wars.setHorizontalScrollBarPolicy(
        Qt.ScrollBarPolicy.ScrollBarAsNeeded
        )

        scroll_star_wars.setVerticalScrollBarPolicy(
         Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        scroll_star_wars.setFixedHeight(450)

        #======================
        # CATÁLOGO HARRY POTTER
        #======================     

        Titulo_harry_potter = QLabel("HARRY POTTER")
        Titulo_harry_potter.setStyleSheet("""
            font-size:28px;
            font-weight:bold;
        """)        
        catalogo_harry_potter = QHBoxLayout()
        catalogo_harry_potter.setSpacing(10)    
        filmes_harry_potter = [
            ("harry1.jpg", "Harry Potter e a Pedra Filosofal"),
            ("harry2.jpg", "Harry Potter e a Câmara Secreta"),
            ("harry3.jpg", "Harry Potter e o Prisioneiro de Azkaban"),
            ("harry4.jpg", "Harry Potter e o Cálice de Fogo"),
            ("harry5.jpg", "Harry Potter e a Ordem da Fênix"),
            ("harry6.jpg", "Harry Potter e o Enigma do Príncipe"),
            ("harry7.jpg", "Harry Potter e as Relíquias da Morte - Parte 1"),
            ("harry8.jpg", "Harry Potter e as Relíquias da Morte - Parte 2")
        ]

        for imagem_arquivo, nome_filme in filmes_harry_potter:

            imagem = QLabel()
            imagem.setPixmap(
                QPixmap(imagem_arquivo).scaled(
                    220,
                    320,
                    Qt.AspectRatioMode.KeepAspectRatio
                )
            )
            imagem.setAlignment(Qt.AlignmentFlag.AlignCenter)

            nome = QLabel(nome_filme)
            nome.setAlignment(Qt.AlignmentFlag.AlignCenter)

            botao = QPushButton(" Assistir")
            botao.setIcon(QIcon("reproduzir.png"))
            botao.setIconSize(QSize(24, 24))
            botao.setStyleSheet(estilo_botao)

            filme = QVBoxLayout()
            filme.addWidget(imagem)
            filme.addWidget(nome)
            filme.addWidget(
                botao,
                alignment=Qt.AlignmentFlag.AlignCenter
            )

            catalogo_harry_potter.addLayout(filme)

            widget_harry_potter = QWidget()
        
        widget_harry_potter.setLayout(catalogo_harry_potter)        
        scroll_harry_potter = QScrollArea()
        scroll_harry_potter.setWidget(widget_harry_potter)
        scroll_harry_potter.setWidgetResizable(True)

        scroll_harry_potter.setHorizontalScrollBarPolicy(
        Qt.ScrollBarPolicy.ScrollBarAsNeeded
        )

        scroll_harry_potter.setVerticalScrollBarPolicy(
         Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        scroll_harry_potter.setFixedHeight(450)

        #======================
        # CATÁLOGO SERIES
        #====================== 

        Titulo_series= QLabel("Séries")
        Titulo_series.setStyleSheet("""
            font-size:28px;
            font-weight:bold;
        """)        
        catalogo_series = QHBoxLayout()
        catalogo_series.setSpacing(10)  

        series = [
            ("stranger.jpg", "Stranger Things"),
            ("breaking.jpg", "Breaking Bad"),
            ("gameofthrones.jpg", "Game of Thrones"),
            ("theoffice.jpg", "The Office"),
            ("friends.jpg", "Friends"),
            ("suits.jpg", "Suits"),
            ("bigbangtheory.jpg", "The Big Bang Theory"),
            ("brooklyn.jpg", "Brooklyn Nine-Nine")
        ]

        for imagem_arquivo, nome_series in series:

            imagem = QLabel()
            imagem.setPixmap(
                QPixmap(imagem_arquivo).scaled(
                    220,
                    320,
                    Qt.AspectRatioMode.KeepAspectRatio
                )
            )
            imagem.setAlignment(Qt.AlignmentFlag.AlignCenter)

            nome = QLabel(nome_series)
            nome.setAlignment(Qt.AlignmentFlag.AlignCenter)

            botao = QPushButton(" Assistir")
            botao.setIcon(QIcon("reproduzir.png"))
            botao.setIconSize(QSize(24, 24))
            botao.setStyleSheet(estilo_botao)

            serie = QVBoxLayout()
            serie.addWidget(imagem)
            serie.addWidget(nome)
            serie.addWidget(
                botao,
                alignment=Qt.AlignmentFlag.AlignCenter
            )

            catalogo_series.addLayout(serie)

            widget_series = QWidget()
        
            widget_series.setLayout(catalogo_series)        
            scroll_series = QScrollArea()
            scroll_series.setWidget(widget_series)
            scroll_series.setWidgetResizable(True)

            scroll_series.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAsNeeded
            )

            scroll_series.setVerticalScrollBarPolicy(
             Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

            scroll_series.setFixedHeight(450)



    # =====================
    # CONTEÚDO COM SCROLL
    # =====================

        conteudo = QWidget()

        principal = QVBoxLayout(conteudo)

        principal.addWidget(titulo)
        principal.addSpacing(20)

        principal.addWidget(titulo_marvel)
        principal.addWidget(scroll_marvel)
        principal.addWidget(titulo_star_wars)
        principal.addWidget(scroll_star_wars)
        principal.addWidget(Titulo_harry_potter)
        principal.addWidget(scroll_harry_potter)
        principal.addWidget(Titulo_series)
        principal.addWidget(scroll_series)
        principal.addSpacing(30)

        principal.addWidget(titulo_pixar)
        principal.addWidget(scroll_pixar)

        principal.addStretch()

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setWidget(conteudo)

        layout_janela = QVBoxLayout()
        layout_janela.addWidget(scroll)

        self.setLayout(layout_janela)


app = QApplication(argv)

janela = MoroFlix()
janela.show()

app.exec()