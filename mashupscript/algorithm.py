import csv


datasetNew = {}
provinceLombardia = ["BG","BS","CO","CR","LC","LO","MN","MI","MB","PV","SO","VA"]

#leggi CSV Operatori
with open('operatoribiologici.csv') as f:
    for riga in csv.DictReader(f, delimiter=';'):
        provincia = riga["PROVINCIA"]
        if provincia in provinceLombardia:
            if provincia not in datasetNew:
                datasetNew[provincia] = {}

            if "operatori_biologici" not in datasetNew[provincia]:
                datasetNew[provincia]["operatori_biologici"] = 0
            datasetNew[provincia]["operatori_biologici"] += 1

            if "operatori_biologici_produzione_vegetale" not in datasetNew[provincia]:
                datasetNew[provincia]["operatori_biologici_produzione_vegetale"] = 0
            if "VEGETAL" in riga["DESCRIZIONE_TIPOLOGIA"]:
                datasetNew[provincia]["operatori_biologici_produzione_vegetale"] += 1

            if "operatori_biologici_produzione_zootecnica" not in datasetNew[provincia]:
                datasetNew[provincia]["operatori_biologici_produzione_zootecnica"] = 0
            if "ZOO" in riga["DESCRIZIONE_TIPOLOGIA"]:
                datasetNew[provincia]["operatori_biologici_produzione_zootecnica"] += 1

            if "operatori_biologici_importatore" not in datasetNew[provincia]:
                datasetNew[provincia]["operatori_biologici_importatore"] = 0
            if "IMPORT" in riga["DESCRIZIONE_TIPOLOGIA"]:
                datasetNew[provincia]["operatori_biologici_importatore"] += 1

            if "operatori_biologici_esportatore" not in datasetNew[provincia]:
                datasetNew[provincia]["operatori_biologici_esportatore"] = 0
            if "ESPORT" in riga["DESCRIZIONE_TIPOLOGIA"]:
                datasetNew[provincia]["operatori_biologici_esportatore"] += 1

            if "operatori_biologici_tipologia_non_specificata" not in datasetNew[provincia]:
                datasetNew[provincia]["operatori_biologici_tipologia_non_specificata"] = 0
            if riga["DESCRIZIONE_TIPOLOGIA"] == "":
                datasetNew[provincia]["operatori_biologici_tipologia_non_specificata"] += 1

            if "operatori_biologici_produttori" not in datasetNew[provincia]:
                datasetNew[provincia]["operatori_biologici_produttori"] = 0
            if "PRODUTTOR" in riga["DESCRIZIONE_TIPO_ATTIVITA"]:
                datasetNew[provincia]["operatori_biologici_produttori"] += 1

            if "operatori_biologici_preparatori" not in datasetNew[provincia]:
                datasetNew[provincia]["operatori_biologici_preparatori"] = 0
            if "PREPARATOR" in riga["DESCRIZIONE_TIPO_ATTIVITA"]:
                datasetNew[provincia]["operatori_biologici_preparatori"] += 1





            '''
            if "date_certificazioni" not in datasetNew[provincia]:
                datasetNew[provincia]["date_certificazioni"] = ""
                datasetNew[provincia]["date_certificazioni"] += riga["DATA_CERTIFICATO"]
                datasetNew[provincia]["date_certificazioni"] += ";"
            '''



#leggi CSV fattoriedidattiche
with open('fattoriedidattiche.csv') as f:
    for riga in csv.DictReader(f, delimiter=';'):
        provincia = riga["PR"].upper()
        if provincia in provinceLombardia:
            if provincia not in datasetNew:
                datasetNew[provincia] = {}

            if "fattorie_didattiche" not in datasetNew[provincia]:
                datasetNew[provincia]["fattorie_didattiche"] = 0
            datasetNew[provincia]["fattorie_didattiche"] += 1

            campi = {"Asilo nido":"asilo_nido",
                     "Scuola infanzia":"scuola_infanzia",
                     "Scuola primaria":"scuola_primaria",
                     "Scuola secondaria I grado":"scuola_secondaria_i_grado",
                     "Scuola secondaria II grado":"scuola_secondaria_ii_grado",
                     "Adulti":"adulti",
                     "Disabili":"disabili",
                     "Anziani":"anziani",
                     "Ristorazione":"ristorazione",
                     "Attivita sportive":"attivita_sportive",
                     "Pernottamento":"pernottamento",
                     "Punto vendita":"punto_vendita",
                     "Azienda bio":"azienda_bio",
                     "Accessibilita disabili":"accessibilita_disabili"
                     }

            for k, v in campi.items():
                if "fattorie_didattiche_servizi_"+v not in datasetNew[provincia]:
                    datasetNew[provincia]["fattorie_didattiche_servizi_"+v] = 0
                if riga[k] == "true":
                    datasetNew[provincia]["fattorie_didattiche_servizi_"+v] += 1




#leggi CSV ambiente
with open('ambiente.csv') as f:
    for riga in csv.DictReader(f, delimiter=','):
        provincia = riga["\ufeffPROVINCIA"]
        if provincia in provinceLombardia:
            if provincia not in datasetNew:
                datasetNew[provincia] = {}

            if "listaPP" not in datasetNew[provincia]:
                datasetNew[provincia]["listaPP"] = []

            if "acque_sotterranee_parametri_nella_norma" not in datasetNew[provincia]:
                datasetNew[provincia]["acque_sotterranee_parametri_nella_norma"] = 0
            if riga["VALORE_NUMERICO_NORMALIZZATO"] < riga["LIMITEDIATTENZIONE"]:
                datasetNew[provincia]["acque_sotterranee_parametri_nella_norma"] += 1

            if "acque_sotterranee_parametri_sopra_limite_attenzione" not in datasetNew[provincia]:
                datasetNew[provincia]["acque_sotterranee_parametri_sopra_limite_attenzione"] = 0
            if riga["VALORE_NUMERICO_NORMALIZZATO"] >= riga["LIMITEDIATTENZIONE"] and riga["VALORE_NUMERICO_NORMALIZZATO"] < riga["LIMITEDILEGGE"]:
                datasetNew[provincia]["acque_sotterranee_parametri_sopra_limite_attenzione"] += 1

            if "acque_sotterranee_parametri_sopra_limite_legge" not in datasetNew[provincia]:
                datasetNew[provincia]["acque_sotterranee_parametri_sopra_limite_legge"] = 0
            if riga["VALORE_NUMERICO_NORMALIZZATO"] >= riga["LIMITEDILEGGE"]:
                datasetNew[provincia]["acque_sotterranee_parametri_sopra_limite_legge"] += 1

            if "acque_sotterranee_punti_prelievo" not in datasetNew[provincia]:
                datasetNew[provincia]["acque_sotterranee_punti_prelievo"] = 0
            if riga["CODICE_PP"] not in datasetNew[provincia]["listaPP"]:
                datasetNew[provincia]["listaPP"].append(riga["CODICE_PP"])
                datasetNew[provincia]["acque_sotterranee_punti_prelievo"] += 1



import json
with open('jsonmashup.json', 'w') as fp:
    json.dump(datasetNew, fp)
'''
#formatta Dataset In CSV
finalCSV = []

campiOperatori = ["operatori_biologici", "operatori_biologici_produzione_vegetale", "operatori_biologici_produzione_zootecnica","operatori_biologici_importatore","operatori_biologici_esportatore","operatori_biologici_tipologia_non_specificata","operatori_biologici_produttori","operatori_biologici_preparatori"]
campiFattorie = ["asilo_nido","scuola_infanzia","scuola_primaria","scuola_secondaria_i_grado","scuola_secondaria_ii_grado","adulti","disabili","anziani","ristorazione","attivita_sportive","pernottamento","punto_vendita","azienda_bio","accessibilita_disabili"]
campiFalde = ["acque_sotterranee_punti_prelievo","acque_sotterranee_parametri_sopra_limite_legge","acque_sotterranee_parametri_sopra_limite_attenzione","acque_sotterranee_parametri_nella_norma"]

for k, v in datasetNew.items():
    rowObject = {}
    rowObject["provincia"] = k
    for campoOperatore in campiOperatori:
        rowObject[campoOperatore] = v[campoOperatore]
    for campoFattoria in campiFattorie:
        rowObject["fattorie_didattiche_servizi_"+campoFattoria] = v["fattorie_didattiche_servizi_" + campoFattoria]
    for campoFalde in campiFalde:
        rowObject[campoFalde] = v[campoFalde]


    finalCSV.append(rowObject)

keys = finalCSV[0].keys()
with open('mashup.csv', 'w') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(finalCSV)
'''