import random
import os

choix_fichier= input("Choissisez le fichier que vous souhaitez ouvrir : ")
ouvre_fichier = open(choix_fichier,"r", encoding='utf8')
lire_fichier = ouvre_fichier.readlines()

#print(lire_fichier)

nombre_max_pers_groupe = int(input("Combien de nombre de personnes max souhaitez-vous par groupe :"))

pers_fichier = len(lire_fichier)
print(pers_fichier)

pers_par_groupe = []


if  pers_fichier % nombre_max_pers_groupe == 0 : 
    nb_groupes = (pers_fichier//nombre_max_pers_groupe)
else: 
    nb_groupes = (pers_fichier//nombre_max_pers_groupe)+1
print(nb_groupes)


# for personne in range(pers_fichier) :
#         if personne>0:
#             pers_par_groupe.extend([pers_par_groupe+1])
#             pers_fichier-=1
#             print(personne)





