import requests
import pandas as pd
from mojang import API
import json
import datetime
import os
import shutil
compteur=1

def getBazaarInfos(lien): #le coeur du programme ! va chercher les infos en temps réel du bazaar
    r = requests.get(lien)
    data = r.json()
    product_info_list = []
    for product_id, product_data in data["products"].items():
        product_info = {"product_id": product_id}
        quick_status = product_data.get("quick_status", {})
        product_info["sell_price"] = quick_status.get("sellPrice", None)
        product_info["buy_price"] = quick_status.get("buyPrice", None)
        product_info_list.append(product_info)
    return product_info_list

def getPlayerInfos(clef_API, UUID): #va chercher les stats du joueur. Il faut la clef d'API à jour + pas trop de demandes
    lien = f"https://api.hypixel.net/player?key={clef_API}&uuid={UUID}"
    r = requests.get(lien)
    data = r.json()
    if "player" in data:
        player_info = {
            "skyblock_combat": data["player"].get("achievements", {}).get("skyblock_combat"),
            "skyblock_harvester": data["player"].get("achievements", {}).get("skyblock_harvester"),
            "skyblock_excavator": data["player"].get("achievements", {}).get("skyblock_excavator"),
            "skyblock_gatherer": data["player"].get("achievements", {}).get("skyblock_gatherer"),
            "skyblock_domesticator": data["player"].get("achievements", {}).get("skyblock_domesticator"),
            "skyblock_dungeoneer": data["player"].get("achievements", {}).get("skyblock_dungeoneer"),
            "skyblock_curator": data["player"].get("achievements", {}).get("skyblock_curator"),
            "skyblock_angler": data["player"].get("achievements", {}).get("skyblock_angler")
        }
    else:
        player_info = {}
    return player_info

def printPlayerInfo(player_info_uuid): #affiche les infos de niveaux du joueur
    print("\nInformations sur le joueur en utilisant son UUID:")
    print(player_info_uuid.get("skyblock_combat", "Aucune information disponible"), " niveaux en combat")
    print(player_info_uuid.get("skyblock_harvester", "Aucune information disponible"), " niveaux en farming")
    print(player_info_uuid.get("skyblock_excavator", "Aucune information disponible"), " niveaux en mining")
    print(player_info_uuid.get("skyblock_gatherer", "Aucune information disponible"), " niveaux en foraging")
    print(player_info_uuid.get("skyblock_domesticator", "Aucune information disponible"), " niveaux en taming")
    print(player_info_uuid.get("skyblock_dungeoneer", "Aucune information disponible"), " niveaux en dongeon")
    print(player_info_uuid.get("skyblock_curator", "Aucune information disponible"), " niveaux en enchanting")
    print(player_info_uuid.get("skyblock_angler", "Aucune information disponible"), " niveaux en fishing")

def data_ref(lien):
    bazaar_info = getBazaarInfos(lien) #créer le fichier de référence (OUTDATED)
    with open('bazaar_ref.json', 'w') as f:
        json.dump(bazaar_info, f)

def data_comp(lien): #créer le fichier de comparaison (OUTDATED)
    bazaar_info = getBazaarInfos(lien)
    with open('bazaar_comp.json', 'w') as f:
        json.dump(bazaar_info, f)

def data_comp_auto():
    dossier_bazaar = r'C:\your_forlder_here\heure'
    fichiers_bazaar = [f for f in os.listdir(dossier_bazaar) if f.startswith('bazaar_') and f.endswith('.json')]
    if not fichiers_bazaar:
        print("Aucun fichier 'bazaar_{heure}.json' trouvé dans le dossier 'heure'.")
        return
    bazaar_info_total = []
    for fichier in fichiers_bazaar:
        chemin_fichier = os.path.join(dossier_bazaar, fichier)
        with open(chemin_fichier, 'r') as f:
            bazaar_info = json.load(f)
            bazaar_info_total.extend(bazaar_info)
    if not bazaar_info_total:
        print("Aucune information de bazaar trouvée dans les fichiers.")
        return
    produits = {}
    for produit in bazaar_info_total:
        product_id = produit['product_id']
        sell_price = produit.get('sell_price', 0)
        buy_price = produit.get('buy_price', 0)
        if product_id not in produits:
            produits[product_id] = {'sell_price': [], 'buy_price': []}
        produits[product_id]['sell_price'].append(sell_price)
        produits[product_id]['buy_price'].append(buy_price)
    bazaar_final = []
    for product_id, prices in produits.items():
        moyenne_achat = sum(prices['buy_price']) / len(prices['buy_price'])
        moyenne_vente = sum(prices['sell_price']) / len(prices['sell_price'])
        bazaar_final.append({'product_id': product_id, 'sell_price': moyenne_vente, 'buy_price': moyenne_achat})
    jour = datetime.date.today().strftime("%Y-%m-%d")
    chemin_fichier_final = os.path.join('Bazaar', f"bazaar_{jour}.json")
    with open(chemin_fichier_final, 'w') as f:
        json.dump(bazaar_final, f)

def recup_data_comp():
    with open('bazaar_comp.json', 'r') as f:
        bazaar_comp_data = json.load(f)
    with open('comp_data', 'w') as comp_file:
        for item in bazaar_comp_data:
            comp_file.write(f"{item['product_id']} ")
            comp_file.write(f"{item['sell_price']} ")
            comp_file.write(f"{item['buy_price']}\n")

def recup_data_comp_auto(): #récupère, créer et gère les Jsons (je comprends plus)
    dossier_bazaar = r'C:\your_forlder_here\heure'
    fichiers_bazaar = [f for f in os.listdir(dossier_bazaar) if f.startswith('bazaar_') and f.endswith('.json')]
    if not fichiers_bazaar:
        print("Aucun fichier 'bazaar_{heure}.json' trouvé dans le dossier 'heure'.")
        return
    bazaar_info_total = []
    for fichier in fichiers_bazaar:
        chemin_fichier = os.path.join(dossier_bazaar, fichier)
        with open(chemin_fichier, 'r') as f:
            bazaar_info = json.load(f)
            bazaar_info_total.extend(bazaar_info)
    if not bazaar_info_total:
        print("Aucune information de bazaar trouvée dans les fichiers.")
    produits = {}
    for produit in bazaar_info_total:
        product_id = produit['product_id']
        sell_price = produit.get('sell_price', 0)
        buy_price = produit.get('buy_price', 0)
        if product_id not in produits:
            produits[product_id] = {'sell_price': [], 'buy_price': []}
        produits[product_id]['sell_price'].append(sell_price)
        produits[product_id]['buy_price'].append(buy_price)
    bazaar_final = []
    for product_id, prices in produits.items():
        moyenne_achat = sum(prices['buy_price']) / len(prices['buy_price'])
        moyenne_vente = sum(prices['sell_price']) / len(prices['sell_price'])
        bazaar_final.append({'product_id': product_id, 'sell_price': moyenne_vente, 'buy_price': moyenne_achat})
    jour = datetime.date.today().strftime("%Y-%m-%d")
    chemin_fichier_final = os.path.join('Bazaar', f"bazaar_{jour}.json")
    with open(chemin_fichier_final, 'w') as f:
        json.dump(bazaar_final, f)

def recup_data_ref():
    with open('bazaar_ref.json', 'r') as f:
        bazaar_ref_data = json.load(f)
    with open('ref_data', 'w') as ref_file:
        for item in bazaar_ref_data:
            ref_file.write(f"{item['product_id']} ")
            ref_file.write(f"{item['sell_price']} ")
            ref_file.write(f"{item['buy_price']}\n")
    
def moyenne_par_item(): 
    jour = datetime.date.today().strftime("%Y-%m-%d")
    chemin_dossier = r'C:\your_forlder_here\Bazaar'
    fichiers_bazaar = [f for f in os.listdir(chemin_dossier) if f.startswith('bazaar_') and f.endswith('.json')]
    stats_par_item = {}
    for fichier in fichiers_bazaar:
        with open(os.path.join(chemin_dossier, fichier), 'r') as f:
            data = json.load(f)
            for item in data:
                item_id = item['product_id']
                prix_achat = item.get('buy_price', 0)
                prix_vente = item.get('sell_price', 0)
                if item_id not in stats_par_item:
                    stats_par_item[item_id] = {
                        'prix_achat': [],
                        'prix_vente': [],
                    }
                stats_par_item[item_id]['prix_achat'].append(prix_achat)
                stats_par_item[item_id]['prix_vente'].append(prix_vente)
    for item_id, stats in stats_par_item.items():
        moyenne_achat = sum(stats['prix_achat']) / len(stats['prix_achat'])
        moyenne_vente = sum(stats['prix_vente']) / len(stats['prix_vente'])
        benef_achat_vente = moyenne_vente - moyenne_achat
        if benef_achat_vente > 0 and moyenne_achat != 0:
            chemin_benef = r'C:\your_forlder_here\benef'
            with open(os.path.join(chemin_benef, f'items_en_benef_{jour}.txt'), 'a') as benef_file:
                benef_file.write(f"Benefice de: {benef_achat_vente} sur: {item_id}\n")
    data_json = {
        "jour": jour,
        "items": []
    }
    for item_id, stats in stats_par_item.items():
        moyenne_achat = sum(stats['prix_achat']) / len(stats['prix_achat'])
        moyenne_vente = sum(stats['prix_vente']) / len(stats['prix_vente'])
        prix_achat_max = max(stats['prix_achat'])
        prix_achat_min = min(stats['prix_achat'])
        prix_vente_max = max(stats['prix_vente'])
        prix_vente_min = min(stats['prix_vente'])
        benef_achat_vente = moyenne_vente - moyenne_achat
        data_json["items"].append({
            "item_id": item_id,
            "moyenne_achat": moyenne_achat,
            "moyenne_vente": moyenne_vente,
            "prix_achat_max": prix_achat_max,
            "prix_achat_min": prix_achat_min,
            "prix_vente_max": prix_vente_max,
            "prix_vente_min": prix_vente_min,
            "benef_achat_vente": benef_achat_vente
        })
    chemin_sortie = r'C:\your_forlder_here\calculs'
    with open(os.path.join(chemin_sortie, f'calculs_benefs_moyenne_{jour}.json'), 'w') as json_file:
        json.dump(data_json, json_file, indent=4)

#compare le prix d'achat actuel avec le prix de vente moyen. En créer un fichier Json et .txt "Faire le {jour}"
def comparer_prix_achat_vente():
    jour = datetime.date.today().strftime("%Y-%m-%d")
    chemin_fichier_bazaar = rf'C:\your_forlder_here\Bazaar\bazaar_{jour}.json'
    chemin_fichier_calculs = rf'C:\your_forlder_here\calculs\calculs_benefs_moyenne_{jour}.json'
    if not os.path.exists(chemin_fichier_bazaar):
        print(f"Le fichier bazaar_{jour}.json n'existe pas dans le dossier Bazaar.")
        return
    if not os.path.exists(chemin_fichier_calculs):
        print(f"Le fichier calculs_benefs_moyenne_{jour}.json n'existe pas dans le dossier Calculs.")
        return
    
    with open(chemin_fichier_bazaar, 'r') as f:
        donnees_bazaar = json.load(f)
        if donnees_bazaar:
            prix_achat_par_item = {item["product_id"]: item.get("buy_price", 0) for item in donnees_bazaar}
        else:
            print(f"Le fichier bazaar_{jour}.json est vide.")
            return

    with open(chemin_fichier_calculs, 'r') as f:
        donnees_calculs = json.load(f)
        if donnees_calculs and "items" in donnees_calculs:
            prix_vente_par_item = {item["item_id"]: item.get("moyenne_vente", 0) for item in donnees_calculs["items"]}
        else:
            print(f"Le fichier calculs_benefs_moyenne_{jour}.json est vide ou ne contient pas de données d'items.")
            return
    items_en_benefice = []
    for item_id, prix_achat in prix_achat_par_item.items():
        if prix_achat == 0:
            continue
        prix_vente = prix_vente_par_item.get(item_id, 0)
        if prix_achat < prix_vente:
            difference = prix_vente - prix_achat
            items_en_benefice.append({
                "item_id": item_id,
                "prix_achat": prix_achat,
                "prix_vente": prix_vente,
                "difference": difference
            })
    chemin_fichier_js = r'C:\your_forlder_here\journalierJS\data_js.js'
    contenu_js = f'const data = {json.dumps({"items_en_benefice": items_en_benefice}, indent=4)};'
    with open(chemin_fichier_js, 'w') as f:
        f.write(contenu_js)
    
    print(f"Le fichier data_js.js a été enregistré sous : {chemin_fichier_js}")

#vérifie si les chemins sont bons
def verifier_et_creer_dossier(chemin):
    if not os.path.exists(chemin):
        os.makedirs(chemin)

#calcule les flips de là maintenant
def flip(lien):
    # Charger les données du bazaar
    response = requests.get(lien)
    bazaar_data = response.json()

    # Chemin du fichier JS
    chemin_fichier_flip = r'C:\your_forlder_here\flip\data_flip.js'
    verifier_et_creer_dossier(os.path.dirname(chemin_fichier_flip))

    # Lire les données existantes du fichier JSON
    if os.path.exists(chemin_fichier_flip) and os.path.getsize(chemin_fichier_flip) > 0:
        with open(chemin_fichier_flip, 'r') as f:
            contenu = f.read().strip()

            # Vérifier et extraire les données JSON existantes
            if contenu.startswith('const data_flips = '):
                contenu_json = contenu[len('const data_flips = '):].strip().rstrip(';')
                try:
                    flips = json.loads(contenu_json)
                except json.JSONDecodeError as e:
                    print(f"Erreur de décodage JSON: {e}")
                    flips = {"flips": []}
            else:
                print("Le fichier ne commence pas par 'const data_flips = '.")
                flips = {"flips": []}
    else:
        # Créer une structure vide si le fichier est inexistant ou vide
        flips = {"flips": []}

    # Mettre à jour les informations avec les données du bazaar
    product_map = {item['product_id']: item for item in flips['flips']}
    
    for flip in flips['flips']:
        product_id = flip['product_id']
        if product_id in bazaar_data['products']:
            quick_status = bazaar_data['products'][product_id]['quick_status']
            flip['buyMovingWeek'] = quick_status.get('buyMovingWeek', 0)
            flip['sellMovingWeek'] = quick_status.get('sellMovingWeek', 0)

    # Écrire les données mises à jour dans le fichier JSON
    with open(chemin_fichier_flip, 'w') as f:
        f.write('const data_flips = ')
        json.dump(flips, f, indent=4)
        f.write(';')

    print(f"Les données de flip ont été mises à jour avec les moving weeks dans {chemin_fichier_flip}")
def data_get_hourly(lien): #va chercher et mettre chaque heure un Json dans le dossier "heure"
    heure_actuelle = datetime.datetime.now().strftime("%H")
    nom_fichier = f"bazaar_{heure_actuelle}.json"
    bazaar_info = getBazaarInfos(lien)
    dossier_heure = r'C:\your_forlder_here\heure'
    if not os.path.exists(dossier_heure):
        os.makedirs(dossier_heure)
    chemin_fichier = os.path.join(dossier_heure, nom_fichier)
    with open(chemin_fichier, 'w') as f:
        json.dump(bazaar_info, f)

def full_auto(lien): #appel de fonctions pour automatiser le tout dans schedule
    recup_data_comp_auto()
    data_get_hourly(lien)
    moyenne_par_item()
    comparer_prix_achat_vente()
    flip(lien)
    print(f"En activité depuis {compteur+1} jours\n")