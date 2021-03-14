import sys
import csv
import math
from operator import itemgetter, attrgetter




def isInt(number):
    try:
        int(number)
        return True
    except:
        print(number + " n'est pas un index valide.")
        return False


def isCsv(fichier):
    if (fichier.split(".")[-1].upper() != "CSV"):
        print(fichier + " n'est pas un fichier csv.")
        return False
    else:
        return True

if __name__ == "__main__":
    if (len(sys.argv) != 3):
        print("Veuillez passer le fichier et l'index de la colonne à comparer.")
        exit
    elif (not isCsv(sys.argv[1])):
        pass
    elif not isInt(sys.argv[2]):
        pass
    else:
        print("ça part")




        


# with open('tp_mushrooms_dataset_150.csv', newline='') as f:
#    reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
#    for row in reader:
#        print(row) 
        

def afficher (nom_du_fichier):
    nb_individus = -1
    with open(nom_du_fichier, newline='') as f:
        reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
        for row in reader:
            nb_individus += 1
        print(row)
    print("Nombre d'individus : " + str(nb_individus))
    
import csv, math

def parseur(filePath):
    csvfile = open(filePath)
    file = csv.reader(csvfile, delimiter=',')
    datas = []
    for row in file:
        datas.append(row)
    return datas

def afficherStats(datas):
    print("Nombre d'individus : " + str(len(datas)-1) + "\n"
    + "Nombre d'attributs : " + str(len(datas[0])) + "\n"
    + "Nombre de prédictions : " + str(5)
    )

'''def distance(individuI, individuN):
    if (len(individuI) != len(individuN)):
        return False
    else:
        dist = 0
        i = 0
        for atribut in individuI:
            if atribut != individuN[i] and type(individuN[i]) == 'str' :
                print('bonjour')
                dist+=1
                i+=1
            else:
              dist += (abs(individuI[atribut[i]] - individuN[atribut[i]])^2)/(max(datas[atribut[i]]))
    return math.sqrt(dist)'''
    

def distance(individuI, individuN):
    if (len(individuI) != len(individuN)):
        return False
    else:
        dist = 0
        i = 0
        for atribut in individuI:
            if atribut != individuN[i]:
                dist+=1
            i+=1
        return math.sqrt(dist)

datas = parseur('tp_mushrooms_dataset_5000.csv')
afficherStats(datas)

#print(distance(datas[9], datas[12]))


#indice 22 = edible ou pas

def KNN (nb_voisins, l_inconnu):
    mangeable = 0
    pas_mangeable = 0
    resultats_distance = []
    temp = []
    print(nb_voisins)
    for i in range (len(datas)) :
        resultats_distance.append((distance(l_inconnu, datas[i]), i, datas[i]))
    plus_proche = sorted(resultats_distance, key=lambda x: x[0])
    for i in range (nb_voisins) :
        print(plus_proche[i])
        print(plus_proche[i][2][22])
        if plus_proche[i][2][22] == "e" :
            mangeable += 1
        else :
            pas_mangeable += 1
    print("parmis les",nb_voisins , "voisins plus proche du champignons que nous avons analysé,", mangeable, "sont mangeable et", pas_mangeable, "ne sont pas mangeable" )
    if mangeable > pas_mangeable :
        print("nous pouvons donc concluer que le champignon est mangeable")
    else :
        print("nous pouvons donc concluer que le champignon n'est pas mangeable")
 

#KNN(100, datas[5010])




def mon_menu():
    ma_continuation = 1
    while ma_continuation == 1 :
        indice = int(input('quel est l indice du champignon que vous voulez determinez ? : \n \n'))
        print(indice)
        voisins = int(input('combien de voisins voulez vous afficher ? : \n \n'))
        KNN(voisins, datas[indice])
        continuer = input('voulez vous continuer ? tapez oui ou non  \n')
        if continuer == 'oui' :
            ma_continuation = 1
        else :
            ma_continuation = 0


def KNN_autre(nb_voisins, l_inconnu, classe):
    mangeable = 0
    pas_mangeable = 0
    resultats_distance = []
    temp = []
    print(nb_voisins)
    for i in range (len(datas)) :
        resultats_distance.append((distance(l_inconnu, datas[i]), i, datas[i]))
    plus_proche = sorted(resultats_distance, key=lambda x: x[0])
    for i in range (nb_voisins) :
        print(plus_proche[i])
        print(plus_proche[i][2][classe])
        if plus_proche[i][2][classe] == plus_proche[0][2][classe] :
            mangeable += 1
        else :
            pas_mangeable += 1
    print("parmis les",nb_voisins , "voisins plus proche du champignons que nous avons analysé,", mangeable, "on la classe", plus_proche[0][2][classe], "et", pas_mangeable, "ont une autre classe" )
    if mangeable > pas_mangeable :
        print("nous pouvons donc conclure que le champignon est de classe ", plus_proche[0][2][classe])
    else :
        print("nous pouvons donc conclure que le champignon n'est pas de classe ",classe)
    
    
 
KNN_autre(100, datas[1], 0)

