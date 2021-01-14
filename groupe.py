import random
import os

choix_fichier= input("Choissisez le fichier que vous souhaitez ouvrir : ")
ouvre_fichier = open(choix_fichier,"r", encoding='utf8')
lire_fichier = ouvre_fichier.readlines()

print(lire_fichier)

nombre_groupe = input("Combien de nombre de personnes souhaitez par groupe :")

team = []
longueur = len(lire_fichier)
print(longueur)

#for number in nombre_groupe:




