# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 20:38:26 2018

@author: ortizca
"""

import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from UIscripts.onihm import Ui_OnitamaGameMenu
from UIscripts.rules import Ui_RulesWindow
from UIscripts.in_game import Ui_InGameWindow
import onitama_backend as ob
import pygame as p


p.init()


# l'approche par héritage simple de la classe QMainWindow (même type de notre fenêtre 
# créée avec QT Designer. Nous configurons après l'interface utilisateur 
# dans le constructeur (la méthode init()) de notre classe

class MonAppli(QtWidgets.QMainWindow):
    def __init__(self):
        """
        classe gérant le lien entre l'IHM et le backend de notre programme.
        self.ui basculera entre un UI de menu principal, de fenêtre des règles, au plateau de jeu.
        self.stage est une instance de la classe plateau (initialisé à 0 car le mode choisi définira comment on instancie le plateau)
        """
        super().__init__()

        self.stage = ob.Plateau(5, 5, 0)
        self.win = False

        self.path_carte = ""

        self.mode = (0, 0)
        self.choix_joueur = [-1, -1, -1]
        self.choix_esprit = [-1, 0]
        self.quel_joueur = 0 #par défaut, le joueur qui commence est défini lors de la création d'un plateau



    def play_music(self, music_path):
        p.mixer.music.load(music_path)  # chargement de la musique
        p.mixer.music.play()  # la musique est jouée



    ####
    """
    les méthodes qui suivent sont toutes des slots connectés à des QPushButtons
    """

    #slots de choix du mode de jeu
    def mode_normal(self):
        self.mode = (1, 0)

    def esprit_vent_calme(self):
        self.mode = (2, 1)

    def esprit_vent_brise_matin(self):
        self.mode = (2, 2)

    def esprit_vent_vent_leger(self):
        self.mode = (2, 3)

    def esprit_vent_tempete(self):
        self.mode = (2, 4)

    def esprit_vent_ouragan(self):
        self.mode = (2, 5)

    def esprit_vent_OMD(self):
        self.mode = (2, 6)

    def voie_maitre(self):
        self.mode = (3, 0)



    #slots correspondants aux pions dans le jeu
    def pion11(self):
        if self.quel_joueur == 0:
            self.choix_joueur[0] = 1

    def pion12(self):
        if self.quel_joueur == 0:
            self.choix_joueur[0] = 2

    def pion13(self):
        if self.quel_joueur == 0:
            self.choix_joueur[0] = 3

    def pion14(self):
        if self.quel_joueur == 0:
            self.choix_joueur[0] = 4

    def roi1(self):
        if self.quel_joueur == 0:
            self.choix_joueur[0] = 0

    def pion21(self):
        if self.quel_joueur == 1:
            self.choix_joueur[0] = 1

    def pion22(self):
        if self.quel_joueur == 1:
            self.choix_joueur[0] = 2

    def pion23(self):
        if self.quel_joueur == 1:
            self.choix_joueur[0] = 3

    def pion24(self):
        if self.quel_joueur == 1:
            self.choix_joueur[0] = 4

    def roi2(self):
        if self.quel_joueur == 1:
            self.choix_joueur[0] = 0


    def esprit(self):
        self.choix_esprit[1] = 1 #on active le fait de bouger l'esprit avec une carte normale




    #slots correspondant aux 5 cartes mises en jeu
    def carte1(self):
        if self.quel_joueur == 0:
            self.choix_joueur[1] = 1
            self.display_carte(1)
            self.choix_joueur[2] = -1 #on force le joueur à choisir un mouvement après avoir choisi la carte
        else:
            self.ui.label.setText("  veuillez choisir une de vos cartes")

    def carte2(self):
        if self.quel_joueur == 0:
            self.choix_joueur[1] = 2
            self.display_carte(2)
            self.choix_joueur[2] = -1
        else:
            self.ui.label.setText("  veuillez choisir une de vos cartes")


    def carte0(self):
        self.ui.label.setText("  veuillez choisir une de vos cartes \n  vous pourrez jouer cette carte au prochain tour")

    def carte3(self):
        if self.quel_joueur == 1:
            self.choix_joueur[1] = 3
            self.display_carte(3)
            self.choix_joueur[2] = -1
        else:
            self.ui.label.setText("  veuillez choisir une de vos cartes")

    def carte4(self):
        if self.quel_joueur == 1:
            self.choix_joueur[1] = 4
            self.display_carte(4)
            self.choix_joueur[2] = -1
        else:
            self.ui.label.setText("  veuillez choisir une de vos cartes")



    #slots correspondant aux mouvement possibles dans la cardbox
    def move1(self):
        self.choix_joueur[2] = 0

    def move2(self):
        self.choix_joueur[2] = 1

    def move3(self):
        self.choix_joueur[2] = 2

    def move4(self):
        self.choix_joueur[2] = 3


    def move1e(self):
        self.choix_esprit[0] = 0

    def move2e(self):
        self.choix_esprit[0] = 1

    def move3e(self):
        self.choix_esprit[0] = 2

    def move4e(self):
        self.choix_esprit[0] = 3

    def move5e(self):
        self.choix_esprit[0] = 4

    def move6e(self):
        self.choix_esprit[0] = 5

    ####
    #tous les slots précédents ne servent qu'à définir des paramètres, des inputs du joueurs.
    #les slots suivants permettent de faire le lien entre ces paramètres choisis et le script onitama_backend.py




    def display_rules(self):
        """
        instancie self.ui comme étant un Ui_RulesWindow
        :return: nothing
        """
        self.ui = Ui_RulesWindow()
        self.ui.setupUi(self)
        connect_buttons_rules(self)
        self.show()



    def main_menu(self):
        """
        instancie self.ui comme étant un Ui_OnitamaGameMenu
        :return: nothing
        """
        self.mode = (0, 0)
        self.ui = Ui_OnitamaGameMenu()
        self.ui.setupUi(self)
        connect_buttons(self)

        pixmap = QtGui.QPixmap("images/onitama.png")
        pal = QtGui.QPalette()
        pal.setBrush(QtGui.QPalette.Background, QtGui.QBrush(pixmap))
        self.ui.container.lower()
        self.ui.container.stackUnder(self)
        self.ui.container.setAutoFillBackground(True)
        self.ui.container.setPalette(pal)
        self.play_music("musiques/Ultrakill.mp3")

        self.show()



    def start_game(self):
        """
        instancie self.ui comme étant un Ui_InGameWindow
        cette méthode instancie aussi self.stage en fonction du mode sélectionné.
        elle charge aussi les images nécessaires à l'IHM dans le dossier images
        :return: nothing
        """
        self.win = False
        if self.mode[0] == 0:
            print("veuillez sélectionner un mode de jeu")
        else :
            self.ui = Ui_InGameWindow()
            self.ui.setupUi(self)
            connect_buttons_ingame(self)

            self.pint_image(self.ui.container, "images/Boardgame.png")

            self.show()

            if self.mode[0] == 1:
                self.path_carte = "images/cartes_base/"
                self.stage = ob.Plateau(5, 5, 0)
                self.stage.remplir_plateau_vanilla()
                self.stage.choisir_cartes(ob.cartes_liste)

            elif self.mode[0] == 2:
                self.path_carte = "images/Esprit_du_Vent/"
                self.stage = ob.Plateau(5, 5, 1)
                self.stage.remplir_plateau_vanilla()
                self.stage.choisir_cartes(ob.cartes_liste, ob.cartes_vent_liste, self.mode[1] - 1)
                self.pint_image(self.ui.espritw, "images/pions/esprit.png")

            elif self.mode[0] == 3:
                self.path_carte = "images/Voie_du_Maitre/"
                self.stage = ob.Plateau(5, 5, 0)
                self.stage.remplir_plateau_vanilla()
                self.stage.choisir_cartes(ob.cartes_sp_liste)

            self.quel_joueur = self.stage.cartes[0].i_debut - 1
            self.ui.label.setText("    C'est au joueur " + str(self.quel_joueur + 1) + " de jouer")

            self.pint_image(self.ui.carte0frame, self.path_carte + self.stage.cartes[0].name + ".png")
            self.pint_image(self.ui.carte1frame, self.path_carte + self.stage.cartes[1].name + ".png")
            self.pint_image(self.ui.carte2frame, self.path_carte + self.stage.cartes[2].name + ".png")
            self.pint_image(self.ui.carte3frame, self.path_carte + self.stage.cartes[3].name + ".png")
            self.pint_image(self.ui.carte4frame, self.path_carte + self.stage.cartes[4].name + ".png")

            self.pint_image(self.ui.pion11w, "images/pions/pionbleu.png")
            self.pint_image(self.ui.pion12w, "images/pions/pionbleu.png")
            self.pint_image(self.ui.pion13w, "images/pions/pionbleu.png")
            self.pint_image(self.ui.pion14w, "images/pions/pionbleu.png")
            self.pint_image(self.ui.roi1w, "images/pions/roibleu.png")
            self.pint_image(self.ui.pion21w, "images/pions/pionrouge.png")
            self.pint_image(self.ui.pion22w, "images/pions/pionrouge.png")
            self.pint_image(self.ui.pion23w, "images/pions/pionrouge.png")
            self.pint_image(self.ui.pion24w, "images/pions/pionrouge.png")
            self.pint_image(self.ui.roi2w, "images/pions/roirouge.png")
            self.pint_image(self.ui.labelw, "images/scroll.png")

            self.hide_boxes()

            self.play_music("musiques/Okami.mp3")
            if self.mode == (2, 6):
                self.play_music("musiques/OMD.mp3")






    def pint_image(self, widget, path):
        """
        cette méthode prend en paramètres un widget à afficher et une direction d'image, et met l'image dans le widget
        :param widget: QWidgets
        :param path: string
        :return: nothing
        """
        pixmap = QtGui.QPixmap(path)
        pal = QtGui.QPalette()
        pal.setBrush(QtGui.QPalette.Background, QtGui.QBrush(pixmap))
        widget.lower()
        widget.stackUnder(self)
        widget.setAutoFillBackground(True)
        widget.setPalette(pal)




    def display_carte(self, ncarte):
        """
        affiche les cartes dans la cardbox (i.d. les mouvements possibles par la carte
        si la carte est esprit du vent, une deuxième cardbox apparait pour proposer les déplacements possibles pour
        l'esprit du vent
        :param ncarte: le numéro de la carte choisie
        :return: nothing
        """
        carte = self.stage.cartes[ncarte]
        N, N_esprit = carte.nb_deplacement_possible, carte.nb_esprit

        if self.quel_joueur == 0:
            coeff = 1
        elif self.quel_joueur == 1:
            coeff = -1

        if not self.mode[0] == 2: #mode normal
            for k in range(N):
                move = carte.moves[k]
                self.ui.move[k].setGeometry(QtCore.QRect(100 - coeff*50*move[1], 100 + coeff*50*move[0], 50, 50))
            for k in range(N, 4):
                self.ui.move[k].setGeometry(QtCore.QRect(-50, -50, 50, 50))
            self.ui.centre.setGeometry(QtCore.QRect(100, 100, 50, 50))

        else: #mode esprit du vent
            for k in range(N): #cardbox des mouvements du pion
                move = carte.moves[k]
                self.ui.move[k].setGeometry(QtCore.QRect(50 - coeff * 25 * move[1], 50 + coeff * 25 * move[0], 25, 25))
            for k in range(N, 4):
                self.ui.move[k].setGeometry(QtCore.QRect(-50, -50, 25, 25))
            self.ui.centre.setGeometry(QtCore.QRect(50, 50, 25, 25))

            if carte.carte_vent:
                for k in range(N_esprit): #cardbox des mouvements de l'esprit
                    move = carte.moves_esprit[k]
                    self.ui.move_2[k].setGeometry(QtCore.QRect(50 - coeff*25*move[1], 50 + coeff*25*move[0], 25, 25))
                for k in range(N_esprit, 6):
                    self.ui.move_2[k].setGeometry(QtCore.QRect(-50, -50, 25, 25))

            else: #empêcher le joueur de bouger l'esprit lorsqu'il utilise une carte normale
                for k in range(6):
                    self.ui.move_2[k].setGeometry(QtCore.QRect(-50, -50, 25, 25))




    def hide_boxes(self):
        """
        permet de cacher les boutons associés aux mouvements dans les cardboxes à la fin du coup d'un joueur
        de cette manière le joueur suivant est forcé de sélectionner une carte pour que les boutons s'affichent à nouveau
        et pour qu'il puisse choisir un déplacement. Sinon, il risque de choisir un déplacement sans la carte
        :return: nothing
        """
        for k in self.ui.move:
            k.setGeometry(QtCore.QRect(-50, -50, 50, 50))
        if self.mode[0] == 2:
            for k in self.ui.move_2:
                k.setGeometry(QtCore.QRect(-50, -50, 50, 50))





    def valider(self):
        """
        fonction principale de l'IHM. c'est elle qui fait tout le lien entre les paramètres et le coup demandé,
        elle vérifie que le coup est valide et en fonction des cas, et réinitialise les paramètres à la fin du coup.
        :return: nothing
        """
        print("valider1")
        if not self.win and (not -1 in self.choix_joueur):
            win = False
            coup_valide = self.stage.tour_joueur(self.stage.joueurs[self.quel_joueur], self.choix_joueur[0], self.choix_joueur[1], self.choix_joueur[2])

            if coup_valide:
                win = self.stage.check_tour(self.stage.joueurs[self.quel_joueur], self.stage.joueurs[(self.quel_joueur + 1) % 2], self.choix_joueur[0])
                pos_deplace = self.stage.joueurs[self.quel_joueur].pieces[self.choix_joueur[0]].coords #retrouve les nouvelles coordonnées de la piece déplacée
                if self.quel_joueur == 0:
                    self.ui.J1[self.choix_joueur[0]].setGeometry(QtCore.QRect(pos_deplace[0]*105, pos_deplace[1]*105, 105, 105))
                    for k in range(5):
                        pos = self.stage.joueurs[1].pieces[k].coords
                        self.ui.J2[k].setGeometry(QtCore.QRect(pos[0]*105, pos[1]*105, 105, 105))
                elif self.quel_joueur == 1:
                    self.ui.J2[self.choix_joueur[0]].setGeometry(QtCore.QRect(pos_deplace[0] * 105, pos_deplace[1] * 105, 105, 105))
                    for k in range(5):
                        pos = self.stage.joueurs[0].pieces[k].coords
                        self.ui.J1[k].setGeometry(QtCore.QRect(pos[0]*105, pos[1]*105, 105, 105))

                self.repint_cards()
                self.quel_joueur = (self.quel_joueur + 1) % 2
                self.ui.label.setText("    C'est au joueur " + str(self.quel_joueur + 1) + " de jouer")

            else:
                self.ui.label.setText("    Ce coup n'est pas valide")

            if win: #déclencher la fin de la partie, et un message de victoire
                self.win = True
                self.ui.label.setText("    La partie est terminée\n  Le joueur "+str((self.quel_joueur+1)%2)+" a gagné\n  cliquez sur menu pour recommencer\n  une partie")

        else:
            self.check_inputs()
        self.hide_boxes()
        self.choix_joueur = [-1, -1, -1]





    def valider2(self):
        """
        redite de valider(), elle est utilisée en mode esprit du vent
        :return: nothing
        """
        if not self.win and (not -1 in self.choix_joueur) and self.choix_esprit[0] != 0:
            win = False
            coup_valide = self.stage.tour_joueur_vent(self.stage.joueurs[self.quel_joueur], self.choix_joueur[0], self.choix_joueur[1], self.choix_joueur[2], self.choix_esprit[0], self.choix_esprit[1])

            if coup_valide:
                win = self.stage.check_tour(self.stage.joueurs[self.quel_joueur], self.stage.joueurs[(self.quel_joueur + 1) % 2], self.choix_joueur[0])
                pos_deplace = self.stage.joueurs[self.quel_joueur].pieces[self.choix_joueur[0]].coords #retrouve les nouvelles coordonnées de la piece déplacée

                if self.quel_joueur == 0: #on met à jour les im des pions adverses, au cas ou l'un d'entre eux est mort ou déplacé par l'esprit
                    self.ui.J1[self.choix_joueur[0]].setGeometry(QtCore.QRect(pos_deplace[0]*105, pos_deplace[1]*105, 105, 105))
                    for k in range(5):
                        pos = self.stage.joueurs[1].pieces[k].coords
                        self.ui.J2[k].setGeometry(QtCore.QRect(pos[0]*105, pos[1]*105, 105, 105))
                elif self.quel_joueur == 1:
                    self.ui.J2[self.choix_joueur[0]].setGeometry(QtCore.QRect(pos_deplace[0] * 105, pos_deplace[1] * 105, 105, 105))
                    for k in range(5):
                        pos = self.stage.joueurs[0].pieces[k].coords
                        self.ui.J1[k].setGeometry(QtCore.QRect(pos[0]*105, pos[1]*105, 105, 105))

                pos = self.stage[0].coords
                self.ui.espritw.setGeometry(QtCore.QRect(pos[0]*105, pos[1]*105, 105, 105))

                self.repint_cards()
                self.quel_joueur = (self.quel_joueur + 1) % 2
                self.ui.label.setText("C'est au joueur " + str(self.quel_joueur + 1) + " de jouer")

            else:
                self.ui.label.setText("Ce coup n'est pas valide")

            if win: #déclencher la fin de la partie, et un message de victoire
                self.win = True
                self.ui.label.setText("  La partie est terminée\n  Le joueur "+str((self.quel_joueur+1)%2)+" a gagné\n  cliquez sur menu pour recommencer\n  une partie")

        elif -1 in self.choix_joueur:
            self.ui.label.setText("  Veuillez sélectionner un pion, \n  une carte et un déplacement")

        self.choix_joueur = [-1, -1, -1]
        self.choix_esprit = [-1, 0]




    def repint_cards(self):
        """
        réaffiche les cartes à la fin d'un tour, car deux d'entre elles ont échangé leurs places
        :return: nothing
        """
        self.pint_image(self.ui.carte0frame, self.path_carte + self.stage.cartes[0].name + ".png")
        self.pint_image(self.ui.carte1frame, self.path_carte + self.stage.cartes[1].name + ".png")
        self.pint_image(self.ui.carte2frame, self.path_carte + self.stage.cartes[2].name + ".png")
        self.pint_image(self.ui.carte3frame, self.path_carte + self.stage.cartes[3].name + ".png")
        self.pint_image(self.ui.carte4frame, self.path_carte + self.stage.cartes[4].name + ".png")
        self.hide_boxes()



    def check_inputs(self):
        """
        vérifie que l'input est complet (que le joueur n'a pas oublié de cliquer sur une carte ou autre)
        :return: booléen indicateur de si c'est bon
        """
        a, b, c = self.choix_joueur
        txt = "    C'est au joueur " + str(self.quel_joueur + 1) + " de jouer\n"
        if a == -1:
            txt += "    choisissez une piece a déplacer\n"
        if b == -1:
            txt += "    choisissez une carte à utiliser\n"
        if c == -1:
            txt += "    choisissez un mouvement dans la\n    cardbox\n"
        self.ui.label.setText(txt)
        if self.win:
            self.ui.label.setText("    La partie est terminée\n  Le joueur "+str((self.quel_joueur)+1)+" a gagné\n  cliquez sur menu pour recommencer\n  une partie")







def connect_buttons(window):
    """
    connecte tous les boutons à l'interface MenuPrincipal
    :param window: MonAppli
    :return: nothing
    """
    window.ui.mode1.clicked.connect(window.mode_normal)
    window.ui.mode21.clicked.connect(window.esprit_vent_calme)
    window.ui.mode22.clicked.connect(window.esprit_vent_brise_matin)
    window.ui.mode23.clicked.connect(window.esprit_vent_vent_leger)
    window.ui.mode24.clicked.connect(window.esprit_vent_tempete)
    window.ui.mode25.clicked.connect(window.esprit_vent_ouragan)
    window.ui.mode26.clicked.connect(window.esprit_vent_OMD)
    window.ui.mode3.clicked.connect(window.voie_maitre)

    window.ui.StartGame.clicked.connect(window.start_game)

    window.ui.rules.clicked.connect(window.display_rules)



def connect_buttons_rules(window):
    """
    connecte le bouton quitter de l'UI Rules
    :param window: MonAppli
    :return: nothing
    """
    window.ui.closeRules.clicked.connect(window.main_menu)


def connect_buttons_ingame(window):
    """
    connecte les boutons du jeu (pieces, cartes, cardboxes...)
    le bouton window.ui.valider sera connecté à une fonction différente selon le mode de jeu
    :param window: MonAppli
    :return: nothing
    """
    window.ui.pion11.clicked.connect(window.pion11)
    window.ui.pion12.clicked.connect(window.pion12)
    window.ui.pion13.clicked.connect(window.pion13)
    window.ui.pion14.clicked.connect(window.pion14)
    window.ui.roi1.clicked.connect(window.roi1)
    window.ui.pion21.clicked.connect(window.pion21)
    window.ui.pion22.clicked.connect(window.pion22)
    window.ui.pion23.clicked.connect(window.pion23)
    window.ui.pion24.clicked.connect(window.pion24)
    window.ui.roi2.clicked.connect(window.roi2)

    window.ui.MenuPrincipal.clicked.connect(window.main_menu)
    #window.ui.valider.clicked.connect(window.valider)

    window.ui.carte0.clicked.connect(window.carte0)
    window.ui.carte1.clicked.connect(window.carte1)
    window.ui.carte2.clicked.connect(window.carte2)
    window.ui.carte3.clicked.connect(window.carte3)
    window.ui.carte4.clicked.connect(window.carte4)

    window.ui.move1.clicked.connect(window.move1)
    window.ui.move2.clicked.connect(window.move2)
    window.ui.move3.clicked.connect(window.move3)
    window.ui.move4.clicked.connect(window.move4)

    if window.mode[0] == 2:
        window.ui.create_card_box()
        window.ui.move1_2.clicked.connect(window.move1e)
        window.ui.move2_2.clicked.connect(window.move2e)
        window.ui.move3_2.clicked.connect(window.move3e)
        window.ui.move4_2.clicked.connect(window.move4e)
        window.ui.move5_2.clicked.connect(window.move5e)
        window.ui.move6_2.clicked.connect(window.move6e)
        window.ui.valider.clicked.connect(window.valider2)
        window.ui.esprit.clicked.connect(window.esprit)

    else:
        window.ui.valider.clicked.connect(window.valider)





        


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MonAppli()
    window.main_menu()
    connect_buttons(window)
    window.show()

    app.exec_()
