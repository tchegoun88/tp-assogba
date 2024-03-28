#Importation des modules 
import pandas as pd
import mysql.connector
from mysql.connector import Error

#Chargement des données
vente = pd.read_excel(r'C:\Users\LAB-MND\Desktop\TP_ASSOGBA\Vente_produit.xlsx')
print(vente.columns)

colonnes = ['code','date','livraison','client','produit','quantite','rabais','mode_livraison']
vente.columns = colonnes
print('----------------------------------------------------------------')
print(vente.columns)

# Chargement du dataframe dans MYSQL
try:
    connexion = mysql.connector.connect(host='localhost',
                                       database='vente_produit',
                                       user='root',
                                       password='')
    if connexion.is_connected():
        print('Connexion à MySQL réussie')
except Error as e:
    print(f"Erreur lors de la connexion à MySQL: {e}")

try:
    cursor = connexion.cursor()

    for i,row in vente.iterrows():
        sql = """INSERT INTO produit(code,date,livraison,client,produit,quantite,rabais,mode_livraison) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
        #print(sql)
        cursor.execute(sql, tuple(row))

    connexion.commit()
    connexion.close()
    print("DataFrame chargé dans MySQL avec succès!")
except Exception as e:
    print(f"Erreur lors du chargement du DataFrame dans MySQL: {e}")







