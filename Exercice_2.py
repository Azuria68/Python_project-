#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''pour exécuter le script : python3 ./Exercice_2.py'''

#importe le module turtle et toutes ses fonctions
from turtle import *

reset()                                         #Recommencer à chaque fois sur un nouveau plan
speed(5)                                        #Dessiner 10x plus vite
setup(800, 800)                                 #Configuration de la taille de la fenêtre
goto(-150, -250)                                #Bouger la tortue en -150/-250
c = 150                                         #Initialise la taille d'un côté


def triangle_equilateral(cote, couleur, angle): #Dessine un triangle
    pencolor('black')                           #Couleur du stylo = noirs
    fillcolor(couleur)                          #Remplissage couleur choisie
    begin_fill()                                #Pour commencer à remplir
    for i in range(3):                          #3 pour les 3 cotés du triange (traçage du triangle)
        forward(cote)                           #On avant de la longueur 'coté'
        left(angle)                             #Avec un angle de 'angle'
    end_fill()                                  #Fin de remplissage 
    up()                                        #On lève le stylo
    forward(cote)                               #Place pour dessiner un motif adjacent
    down()                                      #On repose le stylo


"""
En entrée j'ai :
    cote = la longueur du côté du triangle
    couleur = la couleur de remplissage du triangle
    angle = l'angle selon lequel il faut tourner pour faire un triangle
Le module turtle permet d'ouvrir une interface graphique. Ainsi, toutes les fonctions qu'il utilise permettent de "dessiner" directement.
"""

# dessine un hexagone régulier grâce aux triangles
# triangle_equilateral(2*c, 'white', 120)
# left(60)
# triangle_equilateral(2*c, 'white', 120)
# right(180)
# triangle_equilateral(2*c, 'white', 120)
# left(120)
# forward(2*c)
# right(180)
# triangle_equilateral(2*c, 'white', 120)
# left(60)
# triangle_equilateral(2*c, 'white', 120)
# right(180)
# triangle_equilateral(2*c, 'white', 120)

for i in range(6):                              #On créer une boucle pour créer faire les triangles équilatéraux 6 fois
    triangle_equilateral(2 * c, 'white', 120)   #On appelle triangle_equilateral avec comme valeur 2*c , la couleur blanche et un angle de 120°
    left(60)                                    #Tourne a gauche de 60°

#place pour dessiner les triangles colorés
up()                                         #On leve le stylo
forward(c)                                   #Avance de 'c'
left(120)                                    #Tourne de 120° vers la gauche
forward(c)                                   #Avance de 'c'
# right(180)
down()                                       #On pose le stylo

for i in range(3):                           #répète 3 fois un motif de 2 triangles (l'un bleu l'autre jaune)
    triangle_equilateral(c, 'blue', 120)     #Execution de triangle_equilateral pour les triangles bleu
    right(60)                                #tourne de 60° vers la droite
    triangle_equilateral(c, 'yellow', 120)   #Execution de triangle_equilateral pour les triangles jaunes
    right(60)                                #tourne de 60° vers la droite
    
#place sur l'extérieur de l'hexagone
up()                    #On lève le stylo
left(120)               #Tourne de 120° vers la gauche
forward(c)              #Avance de 'c'
right(120)              #Tourne de 120° vers la droite
down()                  #On pose le stylo

pencolor('white')       #efface les contours (côtés de l'hexagone)
for i in range(3):      #Boucle qui se répète 3 fois
    forward(2 * c)      #On avance de (2*c)
    right(60)           #On tourne de 60° vers la droite
    forward(2 * c)      #On avance de (2*c)
    right(60)           #On tourne de 60° vers la droite

exitonclick()           #Pour sortir de la fenêtre en cliquant
