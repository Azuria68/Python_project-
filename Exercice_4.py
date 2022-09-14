#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''pour exécuter le script : python3 ./Exercice_4.py'''

import re #Importation du module re 
import sys #Importation de sys pour quitter le script en cas d'erreur 

print('\033[1m' + '\033[35m' + "Exercice 4 \n"+ '\033[0m')        #Affiche le numéro de la question + ajout de couleur pour l'esthétique 


#Generation d'un ADN
#L'algorithme suivant génère un code ADN aléatoire de longueur spécifée par l'utilisateur si nécessaire 
#Nous prendrons dans cette exercice une séquence donner de base 
'''
print('\033[1m' + '\033[35m' + "Brin d'ADN" + '\033[0m')          #Ajout de couleur pour l'esthétique 
import random                                                     #On importe le module random
l=int(input("Quelle longueur d'ADN voulez-vous avoir ? : "))      #indication de la taille de la longueur de l'ADN voulue                                          #
code=""                                                           #On attribut a code une chaine de caractère vide
for k in range(0,l):                                              #Boucle de 0 à l (donné par l'utilisateur)
    a=random.randint(1,4)                                                #a est égal a un nombre entre 1 et 4 
    if a==1:                                                      #Si a = 1 code prend la lettre A en plus dans sa chaine de caractère
        code=code + "A"
    if a==2:                                                      #Si a = 2 code prend la lettre T en plus dans sa chaine de caractère
        code=code + "T"
    if a==3:                                                      #Si a = 3 code prend la lettre C en plus dans sa chaine de caractère
        code=code + "C"
    if a==4:                                                      #Si a = 4 code prend la lettr G en plus dans sa chaine de caractère
        code=code + "G"
print (f"Votre ADN est : \n {code}")                              #On affiche l'ADN de l'utilisateur en affichant la variable code

def verif_acid(chaine):
  a = 0
  for acide in chaine:
    if a == 4:
      return True
    elif acide == "A":
      a += 1
      chaine.replace("A", "X")
    elif acide == "T":
      a += 1
      chaine.replace("T", "X")
    elif acide == "C":
      a += 1
      chaine.replace("C", "X")
    elif acide == "G":
      a += 1
      chaine.replace("G", "X")
if a != 4:
  sys.exit()

wait = input("appuyer Enter pour continuer...\n")                 #On attend que l'utilisateur appuie sur une touche pour continuer 
'''

code = "ATGAGTGAACGTCTGAGCATTACCCCGCTGGGGCCGTATATCGGCGCA \n"
print(f"Votre séquence d'ADN est : \n{code}")
#Q1
print('\033[1m' + '\033[35m' + "Question 1\n" + '\033[0m')                           #Affiche le numéro de la question + ajout de couleur pour l'esthétique 

def composition(adn):                                                              #retourne la composition de l'ADN dans un dictionnaire
    seq={}                                                                         #création dictionnaire vide
    for i in adn:                                                                  #i tout au long de mon brin d'adn
        seq[i] = seq.get(i, 0) +1                                                  #stockage dans un dictionnaire i suivi du nombre de fois qu'il apparaît
    return seq                                                                     #retour du disctionnaire

print(f"composition de la séquence : {composition(code)}")                         #Afficher la composition de la séquence

wait = input("appuyer Enter pour continuer...\n")                                  #On attend que l'utilisateur appuie sur une touche pour continuer 
        
#Q2 
print('\033[1m' + '\033[35m' + "Question 2" + '\033[0m')                           #Print le numéro de la question + ajout de couleur pour l'esthétique 

seq = composition(code)
def pourcentGC(seq):                                                               #Calcul du pourcentage de G-C
    x = (seq['C'] + seq['G'])/(seq['A'] + seq['T'] + seq['C'] + seq['G'])                                             #Calcul des acides nucléiques sur l'ensembre pour calculer la fréquence      
    return x*100                                                                   #Pour mettre en pourcentage  
print(f"Pourcentage des liaisons G-C : {pourcentGC(seq)}")                         #Afficher le résultat depuis pourcentGC(seq)
wait = input("appuyer Enter pour continuer...\n")                                  #On attend que l'utilisateur appuie sur une touche pour continuer 

#Q3
print('\033[1m' + '\033[35m' + "Question 3" + '\033[0m')                            #Affiche le numéro de la question + ajout de couleur pour l'esthétique 
def tempFusionHowley(seq):                                                          #Calcul de la température de fusion du brin d'ADN
    GC = pourcentGC(seq)                                                            #Remplacer par GC pour être moins imposant à ecrire dans la formule
    nbbases = seq['A'] + seq['T'] + seq['C'] + seq['G']                             #Additionne chaque base
    if nbbases>10 :                                                                 #Si j'ai plus de 10 bases (condition nécessaire)
        Tm = 67.5 + (0.34 * GC) - (395/nbbases)                                     #Alors Tm prends la valeur calculée par la fonction
    else:                                                                           #Sinon il renvoie un message d'erreur en rouge
        print('\033[31m' + "Pour calculer la température de fusion il faut plus de 10 acide nucléiques" + '\033[0m')
        Tm = 0                                                                      #Dans le cas où il y a moins de 10 acide nucléique, T=0
    return Tm                                                                       #Return la variable Tm
print(f"La température de fusion est de : {tempFusionHowley(seq)} °C ")             #On affiche la température de fusion
wait = input("appuyer Enter pour continuer...\n")                                   #On attend que l'utilisateur appuie sur une touche pour continuer

#Q4
print('\033[1m' + '\033[35m' + "Question 4" + '\033[0m')        #Affiche le numéro de la question + ajout de couleur pour l'esthétique 

def inverser(brin):                                             #Pour faire un brin complémentaire 
    brinbis = []                                                #Création d'une liste vide 
    for i in range(len(brin)):                                  #Boucle faisant la longueur du brin ou on avancera de 1 en 1
        if brin[i] == 'A':                                      #Si le brin à A brinbis ajoute la lettre T dans sa liste (complémentaritée)
            brinbis.append('T')
        elif brin[i] == 'T':                                    #Si le brin à T brinbis ajoute la lettre A dans sa liste (complémentaritée)
            brinbis.append('A')
        elif brin[i] == 'C':                                    #Si le brin à C brinbis ajoute la lettre C dans sa liste (complémentaritée)
            brinbis.append('G')
        else:
            brinbis.append('C')                                 #Sinon il ajoute le brin C (complémentarité)
    brinbis.reverse()                                           #On retourne brinbis
    return brinbis                                              #On retourne la liste

codeinverse = inverser(code)                                    #On créer une variable qui prends pour valeurs le code inverse (la complémentaritée)

def estComplementaire(brin1, brin2):                             # vérifie si 2 brins d'ADN sont complémentaires
    brin1 = list(brin1)                                          #stock des brins1 d'ADN dans des listes
    brin2 = list(brin2)                                          #stock des brins2 d'ADN dans des listes
    brin2.reverse()                                              #retourne le brin à comparer (brin anti-sens)
    if len(brin1) <= len(brin2):                                 #cherche le brin le plus court
        court = brin1                                            #Si la longueur du brin1 est plus courte alors court = brin1
    else:                                       
        court = brin2                                            #Sinon court = brin2
    for i in range(len(court)):                         #pour i jusqu'au bout de la liste la plus courte
        if not (brin1[i] == 'A' and brin2[i] == 'T'     #vérifie si les brins ne sont pas complémentaires (paires AT, CG)
            or brin1[i] == 'C' and brin2[i] == 'G'
            or brin1[i] == 'T' and brin2[i] == 'A'
            or brin1[i] == 'G' and brin2[i] == 'C'):
            return False                                #dans ce cas retourner false
    
    return True                                                  #retourner true s'ils le sont
codetest1 = "TGCGCCGATATACGGCCCCAGCGGGGTAATGCTCAGACGTTCACTCAT"   #Code de test pour la complémentarité (celui ci est complémentaire)
print(f"Test : {estComplementaire(code, codetest1)}")            #Affiche si ils sont complémentaires sous forme booléen
wait = input("appuyer Enter pour continuer...\n")                #On attend que l'utilisateur appuie sur une touche pour continuer

#Q5 
print('\033[1m' + '\033[35m' + "Question 5" + '\033[0m')#Affiche le numéro de la question + ajout de couleur pour l'esthétique 

def ADN2ARN(sequence):                                  #Une fonction qui transcrit un brin d'ADN en ARNm
    ARN = []                                            #Création d'une liste videc
    sequence = code                                     #On assigne a sequence notre séquence ADN, ici code
    for i in range(len(sequence)):                      #Pour i sur toute la longueur de la séquence
        if sequence[i] == 'A':
            ARN.append('U')                             #Mettre un U en face d'un A
        elif sequence[i] == 'T':
            ARN.append('A')                             #Mettre un A en face d'un T
        elif sequence[i] == 'C':
            ARN.append('G')                             #Mettre un G en face d'un C
        else:
            ARN.append('C')                             #Sinon, mettre un C
    ARN = "".join(ARN)                                  #Stock de l'ARNm dans une chaîne de caractères
    return ARN                                          #On return notre liste
print(f"Rappel : Voici votre brin ADN : {code}\n")      #Affiche un rappel sur notre ADN pour le comparer avec notre ARN
print(f"Votre brin d'ARN : {ADN2ARN(codeinverse)}")     #Affiche notre ARN 
wait = input("appuyer Enter pour continuer...\n")       #On attend que l'utilisateur appuie sur une touche pour continuer

#Q6 
print('\033[1m' + '\033[35m' + "Question 6" + '\033[0m')#Affiche le numéro de la question + ajout de couleur pour l'esthétique 

code_genetique = {'UUU': 'F', 'UCU': 'S', 'UAU': 'Y', 'UGU': 'C','UUC': 'F', 'UCC': 'S', 'UAC': 'Y', 'UGC': 'C','UUA': 'L', 'UCA': 'S', 'UAA': '*', 'UGA': '*','UUG': 'L', 'UCG': 'S', 'UAG': '*', 'UGG': 'W','CUU': 'L', 'CCU': 'P', 'CAU': 'H', 'CGU': 'R','CUC': 'L', 'CCC': 'P', 'CAC': 'H', 'CGC': 'R','CUA': 'L', 'CCA': 'P', 'CAA': 'Q', 'CGA': 'R','CUG': 'L', 'CCG': 'P', 'CAG': 'Q', 'CGG': 'R','AUU': 'I', 'ACU': 'T', 'AAU': 'N', 'AGU': 'S','AUC': 'I', 'ACC': 'T', 'AAC': 'N', 'AGC': 'S','AUA': 'I', 'ACA': 'T', 'AAA': 'K', 'AGA': 'R','AUG': 'M', 'ACG': 'T', 'AAG': 'K', 'AGG': 'R','GUU': 'V', 'GCU': 'A', 'GAU': 'D', 'GGU': 'G','GUC': 'V', 'GCC': 'A', 'GAC': 'D', 'GGC': 'G','GUA': 'V', 'GCA': 'A', 'GAA': 'E', 'GGA': 'G','GUG': 'V', 'GCG': 'A', 'GAG': 'E', 'GGG': 'G',}
codeinverse.reverse()
codeinverse2 = "".join(codeinverse)


def search (list,platform):
    for i in range(len(list)):
        if list[i] == platform:
            return True
    return False

def traduction(arn):                                    #Traduire en suite d'acides aminés
    trad = []                                           #Création d'une liste vide
    c = input('Cadre de lecture (0, 1 ou 2): ')         #Choix du cadre de lecture
    c = int(c)                                          #Je donne à c la valeur d'un entier
    arn2 = arn[c:len(arn)]                              #Ma chaîne commence au cadre de lecture, jusqu'à la fin
    if c <= 2 and c >=0 :                               #Si le cadre de lecture est respecté
        ncodon = len(arn2)//3                           #LE NOMBRE DE CODONS EST ÉGAL À LA LONGUEUR DE LA CHAÎNE DIVISÉE PAR 3 (NOMBRE ENTIER)
        for i in range(0, ncodon) :                     #Pour i de la position 0 au dernier codon
            trad.append(code_genetique[arn2[0:3]])      #Ajout à l'arn2 l'acide aminé issu du code génétique qui correspond au premier codon
            arn2 = arn2.replace(arn2[0:3], '', 1)  
            object = '*'                                #On cherche les *, c'est-à-dire les codons stop de la séquence d'acides aminés.
        if search(trad,object):
            print('Un codon stop a été trouvé')         #Si un codon stop est trouvé la sequence d'acides aminés affichés s'arrete a ce codon stop. 
            index=trad.index('*')                                           #S'il n'y a pas de codon stop, l'entierete de la séquence ARNm sera traduite en AA. 
            del trad[index:len(trad)]               
            return(trad)
        else:
             print('Pas de codon stop dans la séquence')                    #Affiche qu'il n'y a pas de codon stop
             return(trad)                                                   #Retour de la liste d'acides aminés
                                                        
    else :
        return 'Erreur, le cadre de lecture est mauvais'
    
print("Essai 1 :")  
print("Voici la séquence en acides aminés correspondant à la séquence de nucléotides :", "\n", traduction(ADN2ARN(codeinverse2)))
print("\nEssai 2 :")
print("Voici la séquence en acides aminés correspondant à la séquence de nucléotides :", "\n", traduction(ADN2ARN(codeinverse2)))
print("\nEssai 3 :")
print("Voici la séquence en acides aminés correspondant à la séquence de nucléotides :", "\n", traduction(ADN2ARN(codeinverse2)))
wait = input("appuyer Enter pour continuer...\n")       #On attend que l'utilisateur appuie sur une touche pour continuer

#Q7

print('\033[1m' + '\033[35m' + "Question 7" + '\033[0m') #Affiche le numéro de la question + ajout de couleur pour l'esthétique 

#Q7a
print('\033[1m' + '\033[35m' + "a)" + '\033[0m') #Affiche le numéro de la question + ajout de couleur pour l'esthétique 

def localiserMotifSimple(sequence, motif, placement):   #Permet de localisé le motif simple
    placement = int(placement)                          #on donne à la variable une valeur d'entier
    sequence = sequence[placement:len(sequence)]        #la sequence est égale à la séquence dans la liste au placement jusqu'à la longueur de celle-ci)
    indexes = [i for i in range(len(sequence))          
               if sequence.startswith(motif, i)]        
    seq = ''                                            
    i = 0                                              
    while i < len(sequence):                            #Tant que i est suppérieur à la longueur de la séquence
        if i in indexes:                                #Si on a i dans indexes alors la seq s'incremente sinon on l'incrémente de la séquence à la position i
            seq += sequence[i:i+len(motif)]   
            i += len(motif)                             
        else:
            seq += sequence[i]                          
            i += 1                                      
    return seq                                          #on return la variable
placement = input('Votre position de début de recherche : ')
motif = input('Choisissez le motif à rechercher essai 1  : ') 
print(localiserMotifSimple(code, motif, placement))
placement = input('Votre position de début de recherche : ')
motif = input('Choisissez le motif à rechercher essai 2: ')
print(localiserMotifSimple(code, motif, placement))
placement = input('Votre position de début de recherche : ')
motif = input('Choisissez le motif à rechercher essai 3: ')
print(localiserMotifSimple(code, motif, placement))
wait = input("appuyer Enter pour continuer...\n")

#Q7b
print('\033[1m' + '\033[35m' + "b)" + '\033[0m') #Affiche le numéro de la question + ajout de couleur pour l'esthétique 

def localiserMotifRE(sequence, motif, placement):                                   #rechercher un motif complexe
    placement = int(placement)                                                      #on donne à la variable une valeur d'entier
    sequence = sequence[placement:len(sequence)]                                    #la nouvelle sequence commence à la position choisie
    pattern = '%s..a(t+|$)'%(motif)                                                 
    #pattern = '(a|t)(c|g)..a(t+|$)'                                                #bonus : trouver tous les motifs qui commencent par A ou T, puis C ou G
    indexes = [(m.start(0), m.end(0)) for m in re.finditer(pattern,sequence)]       #j'indexe le début et la fin de mon motif trouvé dans la séquence autant de fois qu'il s'y trouve
    print("En position(s) : ",indexes)                                              #optionnel : pour vérifier où il se trouve
    start = [indexes[i][0] for i in range(len(indexes))]                            #liste de point de départ du motif
    stop = [indexes[i][1] for i in range(len(indexes))]                             #liste d'indices de fin du motif
    i=0                                                                             #initialisation de la boucle while
    seq = ''                                                                        #création d'une chaine de caracteres vide
    while i < len(sequence):                                                        #tant que i est plus petit que la longueur de mon brin d'ADN
        if i in start:                                                              #si i se trouve dans la liste des points de départ
            seq = seq + '\033[1m' +  '\033[31m' + sequence[i]                       #alors on l'affiche en rouge en gras
            i += 1                                                                  #avance du marqueur de 1
        elif i in stop:                                                             #si i se trouve dans la liste d'indices de fin
            seq += '\033[0m' + sequence[i]                                          #affichage de la suite de la sequence en noir
            i += 1                                                                  #avance du marqueur de 1
        else :                                                                      #sinon 
            seq += sequence[i]                                                      #la sequence ne change pas de couleur
            i += 1                                                                  #javance du marqueur de 1
    return seq + '\033[0m'
placement = input('Votre position de début de recherche : ')                        #retour de la séquence et retour de la couleur d'origine pour la suite
motif = input('Choisissez le motif à rechercher essai 1  : ') 
print(localiserMotifSimple(code, motif, placement))
placement = input('Votre position de début de recherche : ')
motif = input('Choisissez le motif à rechercher essai 2: ')
print(localiserMotifSimple(code, motif, placement))
placement = input('Votre position de début de recherche : ')
motif = input('Choisissez le motif à rechercher essai 3: ')
print(localiserMotifSimple(code, motif, placement))
wait = input("appuyer Enter pour continuer...\n")


#Q8
print('\033[1m' + '\033[35m' + "Question 8" + '\033[0m') #Affiche le numéro de la question + ajout de couleur pour l'esthétique 

def signature(seq, m):                                  #une fonction qui dénombre tous les motifs de taille m dans une séquence donnée
    m = int(m)                                          #m prend la valuer d'un entier
    if m <= 10:                                         #si m < 10
        sign = []                                       #création d'une liste vide
        nm = len(seq)//m                                #le nombre de motif est égal à la logueur de la chaîne divisée par la taille du motif prédéfinie
        seq2={}                                         #création d'un dictionnaire vide
        for a in range(0, nm) :                         #a pour chaque motif
            sign.append(seq[0:m])                       #ajout à la liste le premier motif de taille m
            seq = seq.replace(seq[0:m], '', 1)          #remplacement du premier motif de la séquence par le suivant
        for i in sign:                                  #chaque fois que i se trouve dans la liste
            seq2[i] = seq2.get(i, 0)+1                  #rangement dans le dictionnaire du motif associé au nombre de fois qu'il apparaît
        return seq2                                     #retour du dictionnaire                 
    else:
        return 'Erreur, veuillez saisir un entier entre 1 et 10'                          #si m > 10, renvoi d'un message d'erreur

m = input('De quelle taille doit être la signature ? \nDonnez un nombre entier entre 1 et 10 : ')
print("Je dénombre tous les motifs de la taille choisie : \n", signature(code, m))
m = input('De quelle taille doit être la signature ? \nDonnez un nombre entier entre 1 et 10 : ')
print("Je dénombre tous les motifs de la taille choisie : \n", signature(code, m))
m = input('De quelle taille doit être la signature ? \nDonnez un nombre entier entre 1 et 10 : ')
print("Je dénombre tous les motifs de la taille choisie : \n", signature(code, m))
wait = input("appuyer Enter pour finir...\n")














