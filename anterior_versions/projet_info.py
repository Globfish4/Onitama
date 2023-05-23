import random as rd
import numpy as np



def input_piece(joueur):
    piece = -1
    while piece not in [joueur.pieces[k].numero_pion for k in
                        range(len(joueur.pieces))]:  # on exclue le roi pour ce choix car on suppose qu'il est vivant
        piece = int(input("choisir une pièce : \n 0 : Roi, 1-4 : piece\n"))
    if joueur.i_joueur == 2:
        if piece == 0:
            return piece
        else:
            return 5 - piece
    return piece



def input_carte(i_joueur, plateau):
    if i_joueur == 1:
        j = 0
    else:
        j = 2
    carte = 0
    while carte not in [1, 2]:
        carte = int(input("quelle carte voulez-vous utiliser ? 1 ou 2\n//-1 pour retour//\n"))
        if carte == -1:
            return (-1, -1)
    nb_max = plateau.cartes[j + carte].nb_deplacement_possible
    i = -1

    while i < 0 or i > nb_max:
        i = int(input("quel déplacement?\n//-1 pour retour\n//"))
        if i == -1:
            return (-1, -1)
        if i < 0 or i > nb_max:
            print("déplacement non-existant")
    return j + carte, i - 1


def input_carte_vent(i_joueur, plateau):
    if i_joueur == 1:
        j = 0
    else:
        j = 2
    carte = 0


class Plateau(list):
    def __init__(self, xmax, ymax, mode):
        super().__init__()
        self.xmax = xmax
        self.ymax = ymax
        self.cartes = []
        self.joueurs = []
        self.mode = mode


    def remplir_plateau_vanilla(self):
        # initialise le plateau avec les pions et les joueurs
        self.joueurs.append(Joueur(1))
        self.joueurs.append(Joueur(2))
        R1, R2 = Roi(2, 4, 1, self), Roi(2, 0, 2, self)
        self.append(R1)
        self.append(R2)
        self.joueurs[0].pieces.append(R1)
        self.joueurs[1].pieces.append(R2)
        for k in range(4):
            if k < 2:
                p1, p2 = Pion(k, 4, 1, self, k + 1), Pion(k, 0, 2, self, 5 - k - 1)
            elif k >= 2:
                p1, p2 = Pion(k + 1, 4, 1, self, k + 1), Pion(k + 1, 0, 2, self, 5 - k - 1)
            self.append(p1)
            self.append(p2)
            self.joueurs[0].pieces.append(p1)
            self.joueurs[1].pieces.append(p2)


    def remplir_plateau_vent(self):
        # initialise le plateau avec les pions et les joueurs
        V = Esprit_vent(self)
        self.append(V)
        self.joueurs.append(Joueur(1))
        self.joueurs.append(Joueur(2))
        R1, R2 = Roi(2, 4, 1, self), Roi(2, 0, 2, self)
        self.append(R1)
        self.append(R2)
        self.joueurs[0].pieces.append(R1)
        self.joueurs[1].pieces.append(R2)

        for k in range(4):
            if k < 2:
                p1, p2 = Pion(k, 4, 1, self, k + 1), Pion(k, 0, 2, self, 5 - k - 1)
            elif k >= 2:
                p1, p2 = Pion(k + 1, 4, 1, self, k + 1), Pion(k + 1, 0, 2, self, 5 - k - 1)
            self.append(p1)
            self.append(p2)
            self.joueurs[0].pieces.append(p1)
            self.joueurs[1].pieces.append(p2)


    def choisir_cartes(self, cartes_liste):
        # initialise la liste des cartes
        n = len(cartes_liste)
        L = list(range(n))
        rd.shuffle(L)  # renvoie un arrangement aleatoire de nombres entre 0 et 15

        for k in range(5):
            self.cartes.append(cartes_liste[L[k]])


    def gagner(self, joueur, i_victoire):
        if i_victoire == 1:
            msg = "par la voie de la pierre."
        else:
            msg = "par la voie du ruisseau."
        print("Le joueur " + str(joueur.i_joueur) + " gagne " + msg)


    def tour_joueur(self, joueur):
        valid = False  # indicateur de si le coup demandé par le joueur est possible ou non
        while not valid:
            piece = input_piece(joueur)  # int
            carte, i = input_carte(joueur.i_joueur, self)  # j=0 si joueur1 et 2 si joueur2
            if joueur.i_joueur == 1:
                j = 0
            else:
                j = 2
            if (carte, i) != (-1, -1):
                carte_object = self.cartes[carte]
                pos_initiale = joueur.pieces[piece].coords
                valid = joueur.pieces[piece].deplacer(carte_object, i, joueur.i_joueur)
        self.cartes[carte], self.cartes[0] = self.cartes[0], self.cartes[carte]
        # échange des cartes dans la liste self.cartes
        #### attention à l'ordre d'échange


    def tour_joueur_vent(self, joueur):
        valid = False
        while not valid:
            carte, i = input_carte_vent(joueur.i_joueur, self)
            if joueur.i_joueur == 1:
                j = 0
            else:
                j = 2
            if


    def check_tour(self, joueur, adversaire):
        # 1, vérifier que le pion déplacé n'ait pas atteri sur un autre pion
        # 2, vérifier si le pion déplacé a atteri sur la case royale adverse
        joueur.prendre_pion(adversaire)
        if joueur.condition_victoire(adversaire)[0]:
            self.gagner(joueur, joueur.condition_victoire(adversaire)[1])
            return True
        return False


    def simulation(self):
        # fonction qui decide de quel joueur doit jouer et quand la partie termine
        i_debut = self.cartes[0].i_debut
        Niteration = 0
        fin_partie = False
        print("Le joueur " + str(i_debut) + " commence")

        while not fin_partie:
            if (i_debut + Niteration - 1) % 2 == 0:
                print("###Tour n°" + str(Niteration // 2 + 1) + " joueur 1###\n \n")
                self.tour_joueur(self.joueurs[0])
                fin_partie = self.check_tour(self.joueurs[0], self.joueurs[1])
            else:
                print("###Tour n°" + str(Niteration // 2 + 1) + " joueur 2###\n \n")
                self.tour_joueur(self.joueurs[1])
                fin_partie = self.check_tour(self.joueurs[1], self.joueurs[0])

            Niteration += 1
            if fin_partie == False:
                for k in self.cartes:
                    print(k.name)
                    print(k)
                print(self)


    def __str__(self):
        tab = ""
        for j in range(self.ymax):  # abscisse
            for i in range(self.xmax):  # ordonnée
                chre = 00
                tab += "."
                for piece in self:
                    if list(piece.coords) == list(np.array([i, j])):
                        tab += piece.car()
                        chre += len(piece.car())
                tab += (5 - chre) * " "
                if i == self.xmax - 1:
                    tab += "\n"
        tab += "\n"
        tab += "Cartes du joueur 1 : " + self.cartes[1].name + " " + self.cartes[2].name + "\n"
        tab += "Cartes du joueur 2 : " + self.cartes[3].name + " " + self.cartes[4].name + "\n"
        tab += "Carte du centre : " + self.cartes[0].name
        return tab




class Piece:
    def __init__(self, abscisse, ordonnee, i_joueur, plateau):  # i_joueur = 1 ou 2
        self.__coords = np.array([abscisse, ordonnee])
        self.i_joueur = i_joueur  # en gros titre de joueur 1 joueur 2
        self._plateau = plateau
        self._vivante = True


    @property
    def coords(self):
        return self.__coords


    @property
    def x(self):
        return self.__coords[0]


    @property
    def y(self):
        return self.__coords[1]


    def new_coords(self, val):
        setx = val[0]
        sety = val[1]
        if val[0] < 0 and self._vivante:
            print("Deplacement impossible.")
            return False
        if val[0] > self._plateau.xmax - 1:
            print("Deplacement impossible.")
            return False
        if val[1] < 0 and self._vivante:
            print("Deplacement impossible.")
            return False
        if val[1] > self._plateau.ymax - 1:
            print("Deplacement impossible.")
            return False
        if self.i_joueur != 0:
            if list(val) == list(self._plateau[0].coords):
                print("Espace occupé")
                return False
            for piece in self._plateau.joueurs[self.i_joueur - 1].pieces:
                if list(piece.coords) == list(val):
                    print("Espace occupé")
                    return False

        else:
            n = len(self._plateau)
            for i in range(1, n):
                if list(self._plateau[i].coords) == list(val):
                    if self._plateau[i].car(self._plateau[i])[0] != "R":
                        self._plateau[i].coords, self.coords = self.coords, self._plateau[i].coords
                        print("Le pion " + self._plateau[i].car(self._plateau) + " a échangé sa position avec l'esprit du vent")
                        return True
                    else:
                        print("L'esprit du vent ne peut faire vaciller le roi")
                        return False
        self.__coords = (setx, sety)
        return True


    def deplacer(self, carte, i, i_joueur):  # applique new_coords au pion choisi par le déplacement choisi
        coeff = 1
        if i_joueur == 2:
            coeff = -1
        new_coord = self.coords + coeff * carte.moves[i]
        valid = self.new_coords(new_coord)
        return valid  # retourne un indicateur de si le travail est effectué ou non



class Pion(Piece):
    def __init__(self, abscisse, ordonnee, i_joueur, plateau, num_pion):
        super().__init__(abscisse, ordonnee, i_joueur, plateau)
        self.numero_pion = num_pion


    def mourir(self):
        self._vivante = False
        print("Un disciple du joueur " + str(self.i_joueur) + " a été capturé." + "\n")
        self.__coords = np.array([-1, -1])  # on pose le pion à l'extérieur du plateau


    def car(self):
        return "P" + str(self.i_joueur) + "," + str(self.numero_pion)




class Roi(Piece):
    def __init__(self, abscisse, ordonnee, i_joueur, plateau, num_pion=0):
        super().__init__(abscisse, ordonnee, i_joueur, plateau)
        self.numero_pion = num_pion


    def mourir(self):
        self._vivante = False
        print("Le Maitre a été capturé")
        if self.i_joueur == 1:
            self._plateau.gagner(2, 1)
        else:
            self._plateau.gagner(1, 1)


    def car(self):
        return "R" + str(self.i_joueur)



class Esprit_vent(Piece):
    def __init__(self, plateau):
        super().__init__(2, 2, 0, plateau)


    def car(self):
        return "V"



class Carte:
    def __init__(self, name, moves, i_debut, carte_vent = False):  # moves est la liste des vecteurs de déplacement de la carte
        self.name = name
        self.moves = moves  # contient des tuples de deplacement relatif
        self.nb_deplacement_possible = len(self.moves)
        self.i_debut = i_debut
        self.carte_vent = carte_vent



    def __str__(self):
        if self.carte_vent == False:
            A = np.zeros((5, 5))
            A[2, 2] = -1
            for k in range(self.nb_deplacement_possible):
                A[2 + self.moves[k][1], 2 + self.moves[k][0]] = k + 1
            return str(A)



class Joueur:
    def __init__(self, i_joueur):
        # self.cartes = (0, 0)
        self.pieces = []
        self.i_joueur = i_joueur


    def perdre_pion(self, pion):  # pion est le numero du pion a faire perdre
        # à voir en fonction de comment on gère le fait que le joueur ne puisse plus s'en servir
        self.pieces.pop(pion)
        self.pieces[pion].mourir()


    def prendre_pion(self, other):  # self prend un pion à l'autre joueur
        # cette méthode plutot dans Environnement?
        for k in range(len(self.pieces)):
            for l in range(len(other.pieces)):
                if list(self.pieces[k].coords) == list(other.pieces[l].coords):
                    other.perdre_pion(l)
                    break


    def condition_victoire(self, adversaire):
        if list(self.pieces[0].coords) == list(np.array([2, 0])) and self.i_joueur == 1:
            return True, 2
        if list(self.pieces[0].coords) == list(np.array([2, 4])) and self.i_joueur == 2:
            return True, 2
        if not adversaire.pieces[0]._vivante:  # si le roi adverse est mort
            return True, 1
        return False, 0


###cartes


###cartes vanilla

tigre = Carte("Tigre", [np.array([0, -2]), np.array([0, 1])], 2)
dragon = Carte("Dragon", [np.array([1, 1]), np.array([-1, 1]), np.array([-2, -1]), np.array([2, -1])], 1)
grenouille = Carte("Grenouille", [np.array([1, 1]), np.array([2, 0]), np.array([-1, -1])], 1)
lapin = Carte("Lapin", [np.array([-1, 1]), np.array([1, -1]), np.array([2, 0])], 1)
crabe = Carte("Crabe", [np.array([-2, 0]), np.array([2, 0]), np.array([0, -1])], 2)
elephant = Carte("Elephant", [np.array([-1, 0]), np.array([1, 0]), np.array([-1, -1]), np.array([1, -1])], 1)
oie = Carte("Oie", [np.array([-1, 0]), np.array([1, 0]), np.array([-1, -1]), np.array([1, 1])], 2)
coq = Carte("Coq", [np.array([-1, 0]), np.array([-1, 1]), np.array([1, 0]), np.array([1, -1])], 1)
singe = Carte("Singe", [np.array([1, -1]), np.array([-1, 1]), np.array([-1, -1]), np.array([1, 1])], 2)
mante = Carte("Mante Religieuse", [np.array([-1, -1]), np.array([1, -1]), np.array([0, 1])], 1)
cheval = Carte("Cheval", [np.array([-1, 0]), np.array([0, -1]), np.array([0, 1])], 1)
boeuf = Carte("Boeuf", [np.array([0, -1]), np.array([1, 0]), np.array([0, 1])], 1)
grue = Carte("Grue", [np.array([0, -1]), np.array([-1, 1]), np.array([1, 1])], 2)
sanglier = Carte("Sanglier", [np.array([-1, 0]), np.array([1, 0]), np.array([0, -1])], 1)
anguille = Carte("Anguille", [np.array([-1, -1]), np.array([-1, 1]), np.array([1, 0])], 2)
cobra = Carte("Cobra", [np.array([-1, 0]), np.array([1, -1]), np.array([1, 1])], 2)

##carte sensei path


##carte esprit du vent

aigle = Carte("Aigle", [[np.array([-1, 1]), np.array([1, 1])], [np.array([-2, 2]), np.array([2, 2])]], 1, True)

chauve_souris = Carte("Chauve-souris", [[np.array([0, 1]), np.array([0, -1])],
                                        [np.array([-2, 1]), np.array([-1, 1]), np.array([1, 1]), np.array([2, 1])]], 2,
                      True)

lion = Carte("Lion", [[np.array([-1, -1]), np.array([1, 1])], [np.array([0, 1]), np.array([0, 2])]], 1, True)

pieuvre = Carte("Pieuvre", [[np.array([-1, 1]), np.array([1, -1])],
                             [np.array([0, 1]), np.array([1, 0]), np.array([1, -1]), np.array([0, -1]),
                              np.array([-1, -1])]], 2, True)

scorpion = Carte("Scorpion", [[np.array([1, 1]), np.array([1, -1])],
                               [np.array([-2, 1]), np.array([-1, 2]), np.array([1, 2]), np.array([2, 1])]], 2, True)

faucon = Carte("Faucon", [[np.array([-1, 1]), np.array([-1, -1])],
                           [np.array([-2, 1]), np.array([2, 1]), np.array([2, 0]), np.array([-2, 0])]], 2, True)

araignee = Carte("Araignée", [[np.array([1, 2]), np.array([0, -1])],
                               [np.array([-1, 1]), np.array([0, 1]), np.array([1, 1]), np.array([0, -1])]], 1, True)

rhinoceros = Carte("Rhinocéros", [[np.array([-1, 1]), np.array([0, -1])],
                                   [np.array([0, 1]), np.array([1, 1]), np.array([2, 0]), np.array([-2, 0]),
                                    np.array([-1, 1])]], 1, True)

cartes_liste = [tigre, dragon, grenouille, lapin, crabe, elephant, oie, coq, singe, mante, cheval, boeuf, grue,
                sanglier, anguille, cobra]
carte_vent_liste = [aigle, chauve_souris, lion, pieuvre, scorpion, faucon, araignee, rhinoceros]


if __name__ == "__main__":
    plat = Plateau(5, 5, 1)
    plat.choisir_cartes(cartes_liste)
    plat.remplir_plateau_vent()
    for k in plat.cartes:
        print(k.name)
        print(k)
    print(plat)
    plat.simulation()


