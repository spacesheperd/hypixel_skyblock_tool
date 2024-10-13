from definitions import *
from time import sleep
import schedule
import time
api = API()
clef_API="309a4db2-108e-4b10-9a07-0ab94f5098bc"
compteur=0
lien="https://api.hypixel.net/v2/skyblock/bazaar"
schedule.every(1).hours.do(full_auto, lien="https://api.hypixel.net/v2/skyblock/bazaar")
#toutes les 1 heure on va chercher le prix du Bazaar, on le stocke dans l'heure actuelle, on fait un bazaar_{jour} avec la moy des heures
#on calcul la moyenne sur le nombre de fichiers du jours achat, vente et les min/max pour chaque items
#on compare la moyenne de vente avec le prix d'achat du jour. Si prix d'achat du jour < prix moyen vente alors acheter

while True:
    while True:
        activite = str(input("Inspecter les stats d'un joueur [I]\n Prix de références du bazaar [R]\n Prix de comparaison du bazaar [C]\n Mode automatique ? [A]\n"))
        if activite == "I":
            userinput = str(input("Pseudo : "))
            UUID = api.get_uuid(userinput)
            infos = getPlayerInfos(clef_API, UUID)
            printPlayerInfo(infos)
            break
        elif activite == "R":
            data_ref(lien)
            print("Données exportés dans le bazaar_ref.json")
            sleep(2)
            continuer = str(input("Exporter le tout dans les fichiers txt associés ? [O/N]\n"))
            if continuer == "O":
                recup_data_ref()
                print("Terminé\n")
                sleep(2)
            elif continuer == "N":
                break
            else:
                print("Erreur")
            break
        elif activite == "C":
            data_comp(lien)
            print("Données exportés dans le bazaar_comp.json")
            sleep(2)
            continuer = str(input("Exporter le tout dans les fichiers txt associés ? [O/N]\n"))
            if continuer == "O":
                recup_data_comp()
                print("Terminé\n")
                sleep(2)
            elif continuer == "N":
                break
            else:
                print("Erreur")
            break
        elif activite == "A":
            while True:
                schedule.run_pending()
                time.sleep(1)
        else:
            print("Erreur")
            break