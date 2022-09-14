#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""pour exécuter le script : python3 ./Exercice_3.py"""

lst = [10, 18, 14, 20, 12, 16]					                                 #Liste à tester

def minMaxMoy(liste):						                                     #Fonction qui renverra le tuple
    a = (min(liste), max(liste), sum(liste)/len(liste))                          #On créer une variable a qui aura (le minimum de lst, le maximum de lst, et la somme/la taille (moyenne))
    print('\033[1m' + '\033[35m' + "Déscriptif de la liste : \n" + '\033[0m')    #Couleurs pour l'esthetique 
    print('(min,max,moy)')                                                       #On informe le lecteur des positions de ce qu'il attend 
    print(a)                                                                     #On affiche a

"""
En entrée nous donnons la liste de nombres. 
La fonction stocke dans la variable a un tuple() contenant le minimum de la liste, le maximum de la liste et la somme des entiers sur le nombre total d'arguments (moyenne liste). 
En sortie, la fonction print le tuple().
"""

minMaxMoy(lst)							#appel de la fonction
