# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/cami/PycharmProjects/projet_onitama/rules_onitama.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RulesWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(781, 685)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 801, 631))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 0, 791, 621))
        self.label.setObjectName("label")
        self.closeRules = QtWidgets.QPushButton(self.centralwidget)
        self.closeRules.setGeometry(QtCore.QRect(460, 630, 113, 32))
        self.closeRules.setObjectName("closeRules")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.closeRules.clicked.connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Partie normale\n"
"Chaque joueur possède 4 Pion et un Roi assis sur son trône, votre objectif: éliminer le Roi adverse ou prendre \n"
"possession de son château en asseyant votre Roi sur le trône adverse lorsqu\'il est inoccupé.\n"
" \n"
"Pour vous déplacer, il faut se servir de Cartes. Il y a 5 Cartes de déplacement dans une partie, chaque joueur \n"
"en possède 2 et une 5e est placée au milieu du plateau. \n"
"-Sélectionnez votre Carte\n"
"-Sélectionnez la pièce que vous désirez déplacer  \n"
"-Choisissez un déplacement permis par votre carte\n"
"-Une fois que votre Carte est jouée elle sera échangée avec la carte au milieu du plateau\n"
"\n"
"Il existe en tout 16 Cartes de déplacements, une fois que les 5 cartes de la partie sont distribuée, aucune \n"
"autre carte ne peut-être ajoutée. Vous devez donc vous adapter aux possibilités de déplacement définies au début \n"
"de la partie pour obtenir la victoire !\n"
"\n"
"Esprit du vent\n"
"Ce mode de jeu est conseillé aux personnes maitrisant déjà le mode de jeu Partie Normale. Il reprend les \n"
"règles de la partie normale en rajoutant une pièce spéciale: l\'Esprit du Vent, ainsi que de nouvelle cartes: \n"
"les Carte de l\'Esprit du vent.\n"
"\n"
"L\'Esprit du Vent est une pièce qui n\'appartient à aucun joueur, elle peut en revanche être déplacée par chacun des \n"
"deux joueurs avec une Carte de déplacement lors d\'un tour. L\'Esprit du vent ne peux être éliminé par aucune pièce, \n"
"aucune pièce ne peut être déplacée sur la case où l\'Esprit du vent se situe. Si l\'Esprit du vent se déplace sur une \n"
"case occupée par un Pion, celui-ci échangera sa place avec celui-ci. L\'Esprit du Vent est incapable d\'être déplacé \n"
"sur une case occupé par un roi. Les Cartes de l\'Esprit du Vent sont des Cartes très puissante qui vous permettent de \n"
"déplacer l\'une de vos pièce et l\'Esprit du Vent dans le même tour. Vous pouvez également choisir la puissance de \n"
"l\'Esprit du Vent au début de la partie, plus celui-ci sera puissant, plus les parties seront longues et complexes.\n"
"\n"
"Calme: aucune Carte de l\'Esprit du Vent sur le plateau.\n"
"Brise du matin: 1 Carte de l\'Esprit du Vent sur le plateau.\n"
"Vent léger: 2 Cartes de l\'Esprit du Vent sur le plateau. [Recommandé]\n"
"Tempête: 3 Cartes de l\'Esprit du Vent sur le plateau.\n"
"Ouragan: 4 Cartes de l\'Esprit du Vent sur le plateau.\n"
"ONITAMA DOIT MOURIR. : uniquement des Cartes de l\'Esprit du Vent sur le plateau.\n"
"\n"
"La Voie du Maitre\n"
"Ce mode de jeu spécial reprend les règles d\'une partie normale avec 16 nouvelles Cartes de déplacements pour des \n"
"parties plus imprévisibles.\n"
""))
        self.closeRules.setText(_translate("MainWindow", "close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_RulesWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())