# Onitama
Onitama is a video game project. The objective was to recreate the boardgame Onitama with python and QT5.

To play the game : launch `applicationIHM.py`. It is required to have installed PyQt5 and pygame to execute properly the script.
A main window will appear, with many game options, a rules pannel and a `start game` button.

## 1 Rules (french)

### Partie normale
Chaque joueur possède 4 Pion et un Roi assis sur son trône, votre objectif: éliminer le Roi adverse ou prendre possession de son château en asseyant votre Roi sur le trône adverse lorsqu'il est inoccupé.

Pour vous déplacer, il faut se servir de Cartes. Il y a 5 Cartes de déplacement dans une partie, chaque joueur en possède 2 et une 5e est placée au milieu du plateau.
-Sélectionnez une de vos Cartes
-Sélectionnez la pièce que vous désirez déplacer
-Choisissez un déplacement permis par votre carte
-Une fois que votre Carte est jouée elle sera échangée avec la carte au milieu du plateau

Il existe en tout 16 Cartes de déplacements, une fois que les 5 cartes de la partie sont distribuée, aucune autre carte ne peut-être ajoutée. Vous devez donc vous adapter aux possibilités de déplacement définies au début de la partie pour obtenir la victoire !

### Esprit du vent
Ce mode de jeu est conseillé aux personnes maitrisant déjà le mode de jeu Partie Normale. Il reprend les règles de la partie normale en rajoutant une pièce spéciale: l'Esprit du Vent, ainsi que de nouvelle cartes: les Cartes de l'Esprit du vent.

L'Esprit du Vent est une pièce qui n'appartient à aucun joueur, elle peut en revanche être déplacée par chacun des deux joueurs avec une Carte de déplacement lors d'un tour. L'Esprit du vent ne peut être éliminé par aucune pièce, aucune pièce ne peut être déplacée sur la case où l'Esprit du vent se situe. Si l'Esprit du vent se déplace sur une case occupée par un Pion, celui-ci échangera sa place avec celui-ci. L'Esprit du Vent est incapable d'être déplacé sur une case occupé par un roi. Les Cartes de l'Esprit du Vent sont des Cartes très puissantes qui vous permettent de déplacer l'une de vos pièce et l'Esprit du Vent dans le même tour.
Vous pouvez choisir la puissance de l'Esprit du Vent au début de la partie, plus celui-ci sera puissant, plus les parties seront longues et complexes. La puissance de l'esprit du vent correspond au nombre de cartes de l'Esprit du Vent que vous choisissez de mettre dans la partie.

Calme: aucune Carte de l'Esprit du Vent sur le plateau. Il n'y a que des cartes normales
Brise du matin: 1 Carte de l'Esprit du Vent sur le plateau. Les 4 autres cartes sont des cartes normales
Vent léger: 2 Cartes de l'Esprit du Vent sur le plateau. [Recommandé]
Tempête: 3 Cartes de l'Esprit du Vent sur le plateau.
Ouragan: 4 Cartes de l'Esprit du Vent sur le plateau.
ONITAMA DOIT MOURIR. : uniquement des Cartes de l'Esprit du Vent sur le plateau.

### La Voie du Maitre
Ce mode de jeu spécial reprend les règles d'une partie normale avec 16 nouvelles Cartes de déplacements pour des parties plus imprévisibles.


## 2 Content and installation guide

`images` and `musiques` contain the files displayed by the game. 
`QTfiles` are files edited via QT5 designer, they were used to edit the different UIs of the game. These files are not needed to play the game.
`UIscripts` contains python scripts that describe the UIs of the game. There are 3 UIs, the UI for the main menu, the UI for the rules panel and the Ingame UI. These python scripts were created thanks to QT5 Designer.

`Onitama_backend.py` and `Onitama_complet.py` are other versions of the game. The backend version is the one we wrote before designing the UIs. It is a version playable through the terminal. This version is required when installing the game on your computer because some of its functions are used by the script `applicationIHM.py`.

To summarize, the files needed to play the game properly are : 
```
applicationIHM.py
images
musiques
UIscripts
Onitama_backend.py
```


## 3 To do

This projects needs some update so it can become enjoyable.
- Some fixes in the moves of the wind spirit, particularily the order of movement. The wind spirit should move before the pawns.
- The scroll at the bottom right corner gives information on the moves the player is trying to do. This information should be more important and precise.
- When the player selects either a pawn or a card, these elements should be highlighted so that the player can control at each moment what move he is implementing.
- The ingame UI might not be adapted to every computer. 


