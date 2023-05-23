import random as rd
import numpy as np



def input_piece(joueur):
    """
    demande au joueur quelle piece il veut deplacer
    :param joueur: le joueur en question
    :return: un indice entre 0 et 4
    """
    piece = -1
    while piece not in [joueur.pieces[k].numero_pion for k in range(5)]:  # on exclue le roi pour ce choix car on suppose qu'il est vivant
        piece = int(input("choisir une pièce : \n 0 : Roi, 1-4 : piece "))
    return piece


def input_carte(i_joueur, plateau):
    """
    demande au joueur quelle carte il veut utiliser et quel mouvement de la carte utiliser
    tant que l'input n'est pas valide, il redemande jusqu'à ce que ce soit bon
    :param i_joueur: numéro du joueur (1 ou 2)
    :param plateau: le plateau pour avoir les cartes
    :return: le numéro de la carte et le numéro du déplacement
    """
    if i_joueur==1:
        j=0
    else:
        j=2
    carte = 0
    while carte not in [1, 2]:
        carte = int(input("quelle carte voulez-vous utiliser ? 1 ou 2"))
    nb_max = plateau.cartes[j+carte].nb_deplacement_possible
    i = -1
    while i < 0 or i > nb_max:
        i = int(input("quel déplacement?"))
        if i < 0 or i > nb_max:
            print("déplacement non-existant")
    return carte, i-1





class Plateau(list):
    """
    classe écrite par Luc-André Terrine et Camilo Ortiz
    """
    def __init__(self, xmax, ymax):
        super().__init__()
        self.xmax = xmax
        self.ymax = ymax
        self.cartes = []
        self.joueurs = []



    def remplir_plateau(self):
        """
        méthode d'initialisation du plateau (on remplit le plateau avec deux joueurs et les pieces,
        leurs positions initiales etc)
        :return: rien
        """
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
                p1, p2 = Pion(k, 4, 1, self, k + 1), Pion(k, 0, 2, self,5 - k - 1)
            elif k >= 2:
                p1, p2 = Pion(k + 1, 4, 1, self, k + 1), Pion(k + 1, 0, 2, self,5 - k - 1)
            self.append(p1)
            self.append(p2)
            self.joueurs[0].pieces.append(p1)
            self.joueurs[1].pieces.append(p2)



    def choisir_cartes(self, cartes_liste):
        """
        tire au hasard 5 cartes parmi les 16 définies dans cartes_liste
        et les enregistre dans self.cartes
        :param cartes_liste: liste des 16 cartes existantes
        :return: rien
        """
        # initialise la liste des cartes
        n = len(cartes_liste)
        for k in range(5):
            self.cartes.append(cartes_liste[rd.randint(0, n-1)])


    def gagner(self, joueur):
        """
        fonction pour afficher le gagnant
        :param joueur: le joueur qui a gagné
        :return: rien
        """
        print("Le joueur " + str(joueur) + " gagne.")


    def tour_joueur(self, joueur):
        """
        execute un tour complet du joueur :
        demander la piece, la carte et le mouvement à effectuer, il effectue ce mouvement et échange les cartes
        :param joueur: le joueur qui joue
        :return: rien
        """
        valid = False # indicateur de si le coup demandé par le joueur est possible ou non
        while not valid:
            piece = input_piece(joueur)  # int
            carte, i = input_carte(joueur.i_joueur, self)  # j=0 si joueur1 et 2 si joueur2
            if joueur.i_joueur == 1:
                j = 0
            else:
                j = 2


            carte_object = self.cartes[carte]
            valid = joueur.pieces[piece].deplacer(carte_object, i, joueur.i_joueur)

        self.cartes[carte + j], self.cartes[0] = self.cartes[0], self.cartes[carte + j]
        # échange des cartes dans la liste self.cartes
        #### attention à l'ordre d'échange


    def check_tour(self, joueur, adversaire):
        """
        vérifie les conditions de victoire
        :param joueur: le joueur qui vient je jouer
        :param adversaire: son adversaire
        :return: un booléen True si une condition de victoire est atteinte
        """
        # 1, vérifier que le pion déplacé n'ait pas atteri sur un autre pion
        # 2, vérifier si le pion déplacé a atteri sur la case royale adverse
        joueur.prendre_pion(adversaire)

        if joueur.condition_victoire(adversaire):
            self.gagner(joueur)
            return True
        return False


    def simulation(self):
        """
        coordonne les tours des joueurs pour qu'ils jouent chacun leur tour.
        print aussi l eplateau pour que le joueur puisse le voir
        :return: rien
        """
        # fonction qui decide de quel joueur doit jouer et quand la partie termine
        Niteration = 0
        fin_partie = False
        while not fin_partie:
            if Niteration % 2 == 0:
                print("###Tour n°" + str(Niteration // 2 + 1) + " joueur 1###\n \n")
                self.tour_joueur(self.joueurs[0])
                fin_partie = self.check_tour(self.joueurs[0], self.joueurs[1])
            else:
                print("###Tour n°" + str(Niteration // 2 + 1) + " joueur 2###\n \n")
                self.tour_joueur(self.joueurs[1])
                fin_partie = self.check_tour(self.joueurs[1], self.joueurs[0])
            Niteration += 1
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
    """
    classe ecrite par Luc-André Terrine, de même que les deux classes fille
    """
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
        """
        vérifie que les nouvelles coordonnées soient bien dans les limites du terrain
        :param val: tuple contenant les nouvelles coordonnées de la piece
        :return: rien
        """
        setx = val[0]
        sety = val[1]
        if val[0] < 0 and self._vivante:
            print("Deplacement impossible.")
            return False
        if val[0] > self._plateau.xmax-1:
            print("Deplacement impossible.")
            return False
        if val[1] < 0 and self._vivante:
            print("Deplacement impossible.")
            return False
        if val[1] > self._plateau.ymax-1:
            print("Deplacement impossible.")
            return False
        self.__coords = (setx, sety)
        return True


    def deplacer(self, carte, i, i_joueur):  # applique new_coords au pion choisi par le déplacement choisi
        """
        déplace une piece en mettant à jour ses coordonnées en appelant new_coords()
        :param carte: instance de la classe Cartes
        :param i: indice correspondant au déplacement demandé par le joueur
        :param i_joueur: indice (1 ou 2) correspondant au joueur qui joue
        :return: valid, un indicateur de si la piece a bien été déplacée
        """
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
        """
        fait mourir le pion en switchant son indicateur _vivante a False, et en le positionnant
        à l'extérieur du plateau
        :return: rien
        """
        self._vivante = False
        self.__coords = np.array([-1, -1])  # on pose le pion à l'extérieur du plateau


    def car(self):
        return "P" + str(self.i_joueur) + "," + str(self.numero_pion)



class Roi(Piece):
    def __init__(self, abscisse, ordonnee, i_joueur, plateau, num_pion = 0):
        super().__init__(abscisse, ordonnee, i_joueur, plateau)
        self.numero_pion = num_pion


    def mourir(self):
        """
        fait mourir le roi en terminant le jeu et en activant la fonction .gaagner()
        :return: rien
        """
        self._vivante = False
        if self.i_joueur == 1:
            self._plateau.gagner(2)
        else:
            self._plateau.gagner(1)


    def car(self):
        return "R" + str(self.i_joueur)




class Carte:
    """
    classe ecrite par Camilo Ortiz
    """
    def __init__(self, name, moves):  # moves est la liste des vecteurs de déplacement de la carte
        self.name = name
        self.moves = moves  # contient des tuples de deplacement relatif
        self.nb_deplacement_possible = len(self.moves)


    def __str__(self):
        A = np.zeros((5, 5))
        A[2, 2] = -1
        for k in range(self.nb_deplacement_possible):
            A[2+self.moves[k][1], 2+self.moves[k][0]] = k + 1
        return str(A)







class Joueur:
    """
        classe ecrite par Camilo Ortiz
    """
    def __init__(self, i_joueur):
        # self.cartes = (0, 0) LA veut pas
        self.pieces = []
        self.i_joueur = i_joueur


    def perdre_pion(self, pion):  # pas sur que cette fonction soit nécessaire si on bouge le pion hors du plateau
        # à voir en fonction de comment on gère le fait que le joueur ne puisse plus s'en servir
        """
        enleve le pion de la liste de pieces du joueur
        :param pion: le pion a enlever
        :return: rien
        """
        self.pieces.pop(pion.num_pion)
        pion.mourir()


    def prendre_pion(self, other):  # self prend un pion à l'autre joueur
        # cette méthode plutot dans Environnement?
        for k in self.pieces:
            for l in other.pieces:
                if list(k.coords) == list(l.coords):
                    other.perdre_pion(l)


    def condition_victoire(self, adversaire):
        """
        conditions de victoire : le roi adverse meurt ou son trone est occupé
        :param adversaire: l'adversaire du joueur
        :return: un indicateur de si une des conditions de victoire est atteinte
        """
        if list(self.pieces[0].coords) == list(np.array([2, 0])) and self.i_joueur == 1:
            return True
        if list(self.pieces[0].coords) == list(np.array([2, 4])) and self.i_joueur == 2:
            return True
        if not adversaire.pieces[0]._vivante:  # si le roi adverse est mort
            return True
        return False




tigre = Carte("Tigre", [np.array([0, -2]), np.array([0, 1])])
dragon = Carte("Dragon", [np.array([1, 1]), np.array([-1, 1]), np.array([-2, -1]), np.array([2, -1])])
grenouille = Carte("Grenouille", [np.array([1, 1]), np.array([2, 0]), np.array([-1, -1])])
lapin = Carte("Lapin", [np.array([-1, 1]), np.array([1, -1]), np.array([2, 0])])
crabe = Carte("Crabe", [np.array([-2, 0]), np.array([2, 0]), np.array([0, -1])])
elephant = Carte("Elephant", [np.array([-1, 0]), np.array([1, 0]), np.array([-1, -1]), np.array([1, -1])])
oie = Carte("Oie", [np.array([-1, 0]), np.array([1, 0]), np.array([-1, -1]), np.array([1, 1])])
coq = Carte("Coq", [np.array([-1, 0]), np.array([-1, 1]), np.array([1, 0]), np.array([1, -1])])
singe = Carte("Singe", [np.array([1, -1]), np.array([-1, 1]), np.array([-1, -1]), np.array([1, 1])])
mante = Carte("Mante Religieuse", [np.array([-1, -1]), np.array([1, -1]), np.array([0, 1])])
cheval = Carte("Cheval", [np.array([-1, 0]), np.array([0, -1]), np.array([0, 1])])
boeuf = Carte("Boeuf", [np.array([0, -1]), np.array([1, 0]), np.array([0, 1])])
grue = Carte("Grue", [np.array([0, -1]), np.array([-1, 1]), np.array([1, 1])])
sanglier = Carte("Sanglier", [np.array([-1, 0]), np.array([1, 0]), np.array([0, -1])])
anguille = Carte("Anguille", [np.array([-1, -1]), np.array([-1, 1]), np.array([1, 0])])
cobra = Carte("Cobra", [np.array([-1, 0]), np.array([1, -1]), np.array([1, 1])])

cartes_liste = [tigre,dragon,grenouille,lapin,crabe,elephant,oie,coq,singe,mante,cheval,boeuf,grue,sanglier,anguille,cobra]



if __name__ == "__main__":
    plat = Plateau(5, 5)
    plat.choisir_cartes(cartes_liste)
    plat.remplir_plateau()
    for k in plat.cartes:
        print(k.name)
        print(k)
    print(plat)
    plat.simulation()
