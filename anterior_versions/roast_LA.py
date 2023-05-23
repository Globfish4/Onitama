import PyQt5.QtWidgets as widg
from PyQt5.QtCore import *
import sys









app = widg.QApplication(sys.argv)

#fen = widg.QMainWindow()
#fen.setWindowTitle("super méga jeu trop bien ONITAMA")
#fen.resize(840, 480)
#fen.show()


#button = widg.QPushButton("Roast LA", fen)
#button.show()
#fen.button.core.clicked(roast)





class MyForm(widg.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.the_button = widg.QPushButton("roast LA", self)
        self.the_button.setGeometry(QRect(80, 80, 50, 100))
        self.the_button.show()
        self.the_button.clicked.connect(self.test)
        self.setCentralWidget(self.the_button)

    def test(self):
        print("LA Sucks at Smash Ultimate\n et j'aime les fraises")



fen = MyForm()
fen.resize(840, 480)
fen.show()





app.exec_()
