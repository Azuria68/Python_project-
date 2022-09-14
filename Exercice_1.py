#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''pour exécuter le script : python3 ./Exercice_1.py'''

#Création des listes
liste = [1,1,1,2,3,3,1,5,10,10,10]
liste_test = [1,1,1,2,4,4,3,3,1,5,10,10]
liste_test2 = [1,1,1,2,4,4,3,3,5,10,10]

#Q1
def comprime(data):                 #Cette fonction permet de supprime les doublons d'une liste
    data = data[:]                  #La variable reste locale
    i = 0                           #Nous avons l'initialisation de la boucle while
    while i < len(data)-1 :         #Tant que i n'est pas au bout de la liste
        if data[i] == data[i+1]:    #Si i est égale à i+1
            del data[i]             #Supprimer i de la liste
        else:                       #Sinon
            i = i+1                 #Avance le compteur de 1
    return data                     #Pour finir on retourne la liste

"""
La fonction supprime les doublons dans une liste.
Ainsi, nous allons lui donner comme argument la liste à tester, puis, la modifier de manière locale.
Tout au long de la liste, nous procesons à la suppressions des éléments de la liste s'il sont identiques au suivant.
Sinon, j'avance le marqueur de 1 et je teste l'élément suivant.
Enfin, on retourne la nouvelle liste.
"""

#Q2
def compte(data):                        #Cette fonction compte le nombre de doublon les supprime et indique la quantité de doublon
    compte = 0                           #Initialisation du compteur de doublons
    sortie1 = []                         #initialisation d'une liste vide
    sortie1.append(data[0])              #On ajoute data[0] à notre liste sortie1
    for i in data:                       #Pour i dans data
        a = i                            #on ajoute une variable a qui prend la valeur de i 
        if sortie1[-1] != a:             #Si la sortie est différente de a  (le nombre qui suit)
            sortie1.extend([compte,a])   #On agrandit la taille de la liste grâce a compte et a 
            compte=1                     #Et si la condition est validée, compte prends la valeur 1
        else:                            #Sinon 
            compte += 1                  #Compte incrémente de 1 jusqu'à ce que la condition soit validée
    sortie1.append(compte)               #On ajoute ensuite à la liste sortie1 (compte)
    return sortie1                       #Et on fini par return notre liste

"""
La fonction efface les doublons en comptant et affichant le nombre de fois où l'élément apparait.
On lui donne la liste à tester comme argument.
Durant la boucle for, on demande à pyhton si le nombre suivant est différent, si c'est le cas, compte prends la valeur 1
Si ce n'est pas le cas, compte augmente de 1 tant que la condition n'est pas validée. 
"""

#AFFICHAGE :
print('\033[1m' + '\033[35m' + "Fonction comprime" + '\033[0m')                                                 #Couleurs pour l'esthétique 
print(f"la liste comprimer est : \n\n{comprime(liste)}\n")                                                      #j'utilise print(f') pour afficher une variable
print(f"Avec d'autres listes pouvant créer des erreurs : \n\n{comprime(liste_test)}, \n{comprime(liste_test2)}")#J'utilise \n pour que ce soit plus visible 

print('\033[1m' + '\033[35m' + "\nFonction compte" + '\033[0m')     #Couleurs pour esthétique 
print(f"la liste compté est : \n\n{compte(liste)}")